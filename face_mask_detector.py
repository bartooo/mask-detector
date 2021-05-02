from typing import Optional
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
from dataset import Dataset


class FaceMaskDetector:
    def __init__(
        self,
        class_names: str,
        model_path: Optional[str] = None,
        data_dir: Optional[str] = None,
        val_split: Optional[float] = None,
        seed: Optional[int] = None,
        img_height: Optional[int] = None,
        img_width: Optional[int] = None,
        batch_size: Optional[int] = None,
        epochs: Optional[int] = None,
    ) -> None:
        """

        Args:
            class_names (str): names of possible classes
            model_path (str): path to trained model
            data_dir (str): address to directory of data files
            val_split (float): percentage of data that will be in validation dataset
            seed (int): random seed for shuffling and transformations
            img_height (int): height to resize images to after they are read from disk
            img_width (int): width to resize images to after they are read from disk
            batch_size (int): size of batches of data
            epochs (int): number of training epochs
        """
        self._class_names = class_names

        if model_path is None:
            self._ds = Dataset(
                data_dir, val_split, seed, img_height, img_width, batch_size
            )
            self._epochs = epochs

            self._create_model()
            self._compile_model()
            self._train_model()
        else:
            self._model = keras.models.load_model(model_path)

    def _create_model(self) -> None:
        data_augmentation = keras.Sequential(
            [
                layers.experimental.preprocessing.RandomFlip(
                    "horizontal",
                    input_shape=(self._ds.img_height, self._ds.img_width, 3),
                ),
                layers.experimental.preprocessing.RandomRotation(0.1),
                layers.experimental.preprocessing.RandomZoom(0.1),
            ]
        )
        self._model = Sequential(
            [
                data_augmentation,
                layers.experimental.preprocessing.Rescaling(
                    1.0 / 255, input_shape=(self._ds.img_height, self._ds.img_width, 3)
                ),
                layers.Conv2D(16, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(32, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(64, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Dropout(0.2),
                layers.Flatten(),
                layers.Dense(128, activation="relu"),
                layers.Dense(len(self._class_names)),
            ]
        )

    def _compile_model(self) -> None:
        self._model.compile(
            optimizer="adam",
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

    def _train_model(self) -> None:
        self._history = self._model.fit(
            self._ds.train_ds, validation_data=self._ds.val_ds, epochs=self._epochs
        )

    def save_model(self, path: str) -> None:
        self._model.save(path, overwrite=True)

    def get_model_summary(self):
        return self._model.summary()

    def predict_img(self, img):
        """
        Predicts to which class belongs given image array.

        Predicted class - either 'with_mask' or 'without_mask' string.
        Confidence - percentage of model's confidence of classification.
        """
        img_array = keras.preprocessing.image.img_to_array(img)
        batch = tf.expand_dims(img_array, 0)
        predictions = self._model.predict(batch)
        score = tf.nn.softmax(predictions[0])
        predicted_class = self._class_names[np.argmax(score)]
        confidence = 100 * np.max(score)
        return predicted_class, float(confidence)

    @property
    def history(self):
        return self._history
