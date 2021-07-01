from typing import Optional, Any, Tuple
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
from ServerDetector.dataset import Dataset
import cv2
from ServerDetector.parameters import (
    IMG_WIDTH,
    IMG_HEIGHT,
    EPOCHS,
    SCALE_FACTOR,
    MIN_SIZE,
    MIN_NEIGHBORS,
    COLOR_DICT,
    CLASS_NAMES,
)


class FaceMaskDetector:
    def __init__(
        self,
        face_detector_path: str,
        ds: Optional[Dataset] = None,
        model_path: Optional[str] = None,
    ) -> None:
        """

        Args:
            ds (Dataset): dataset used by model
            face_detector_path (str): path to face detector which will be used
            model_path (str): path to trained model
        """

        self._face_detector = cv2.CascadeClassifier(face_detector_path)

        if model_path is not None:
            self._model = keras.models.load_model(model_path)

        if ds:
            self._ds = ds

    def create(self) -> None:
        """Function creates model, compiles it and trains."""
        self._create_model()
        self._compile_model()
        self._train_model()

    def _create_model(self) -> None:
        """Function creates model."""
        data_augmentation = keras.Sequential(
            [
                layers.experimental.preprocessing.RandomFlip(
                    "horizontal", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
                ),
                layers.experimental.preprocessing.RandomRotation(0.1),
                layers.experimental.preprocessing.RandomZoom(0.1),
            ]
        )
        self._model = Sequential(
            [
                data_augmentation,
                layers.experimental.preprocessing.Rescaling(1.0 / 255),
                layers.Conv2D(16, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(32, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(64, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Dropout(0.2),
                layers.Flatten(),
                layers.Dense(128, activation="relu"),
                layers.Dense(len(CLASS_NAMES)),
            ]
        )

    def _compile_model(self) -> None:
        """Function compiles model."""
        self._model.compile(
            optimizer="adam",
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

    def _train_model(self) -> None:
        """Function trains model."""
        self._history = self._model.fit(
            self._ds.train_ds, validation_data=self._ds.val_ds, epochs=EPOCHS
        )

    def save_model(self, path: str) -> None:
        """Function saves model.

        Args:
            path (str): path in which model will be saved
        """
        self._model.save(path, overwrite=True)

    def get_model_summary(self) -> Any:
        """Function returns summary of model.

        Returns:
            Any: summary of model.
        """
        return self._model.summary()

    def _detect_faces(self, img_array: np.array) -> Any:
        """Function detects faces on given image.

        Args:
            img_array (np.array): image to detect faces from model.

        Returns:
            Any: positions of faces
        """
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        rects = self._face_detector.detectMultiScale(
            gray,
            scaleFactor=SCALE_FACTOR,
            minNeighbors=MIN_NEIGHBORS,
            minSize=MIN_SIZE,
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        return rects

    def _draw_info_on_image_with_face(
        self, img_haar: np.array, x: int, y: int, w: int, h: int, predicted_class: str
    ) -> None:
        """Function draws info on faces.

        Args:
            img_haar (np.array): image after haar face detection
            x (int): x coordinate
            y (int): y coordinate
            w (int): width of rectangle
            h (int): height of rectangle
            predicted_class (str): name of predicted class
        """
        # draw the face bounding box on the image
        cv2.rectangle(img_haar, (x, y), (x + w, y + h), COLOR_DICT[predicted_class], 3)

    def _draw_info_on_image_without_face(
        self, predicted_class: str, img_haar: np.array
    ) -> None:
        """[summary]

        Args:
            predicted_class (str): [description]
            img_haar (np.array): [description]
        """
        textsize = cv2.getTextSize(predicted_class, cv2.FONT_HERSHEY_DUPLEX, 2, 1)[0]
        cv2.putText(
            img_haar,
            predicted_class,
            (
                (img_haar.shape[1] - (textsize[0] // 2)) // 2,
                (img_haar.shape[0] + (textsize[1] // 2)) // 2,
            ),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (0, 0, 0),
            3,
        )

    def predict_img(self, img_array: np.array) -> Tuple[str, float, np.array]:
        """
        Predicts to which class belongs given image array.

        Predicted class - either 'with_mask' or 'without_mask' string if face was detected, 'no_face_detected' otherwise.
        Confidence - percentage of model's confidence of classification.
        """
        # detect faces in image
        rects = self._detect_faces(img_array)
        predicted_class = ""
        confidence = 100.0
        img_haar = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        # loop over the bounding boxes
        for (x, y, w, h) in rects:
            # get only the face area
            face_img = img_haar[y : y + h, x : x + w]
            # resize the face area
            face_img = cv2.resize(face_img, (IMG_WIDTH, IMG_HEIGHT))
            batch = tf.expand_dims(face_img, 0)
            predictions = self._model.predict(batch)
            score = tf.nn.softmax(predictions[0])
            predicted_class = CLASS_NAMES[np.argmax(score)]
            confidence = 100 * np.max(score)
            self._draw_info_on_image_with_face(img_haar, x, y, w, h, predicted_class)

        if len(rects) == 0:
            predicted_class = "NO FACE"
            self._draw_info_on_image_without_face(predicted_class, img_haar)
        elif len(rects) > 1:
            predicted_class = "MULTIPLE FACES"
            self._draw_info_on_image_without_face(predicted_class, img_haar)
        return (
            predicted_class,
            float(confidence),
            cv2.cvtColor(img_haar, cv2.COLOR_RGB2BGR),
        )
