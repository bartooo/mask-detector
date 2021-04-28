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
        data_dir: Optional[str] = None,
        val_split: Optional[float] = None,
        seed: Optional[int] = None,
        img_height: Optional[int] = None,
        img_width: Optional[int] = None,
        batch_size: Optional[int] = None,
        num_classes: Optional[int] = None,
        epochs: Optional[int] = None,
        model_path: Optional[str] = None,
    ) -> None:
        """

        Args:
            data_dir (str): address to directory of data files
            val_split (float): percentage of data that will be in validation dataset
            seed (int): random seed for shuffling and transformations
            img_height (int): height to resize images to after they are read from disk
            img_width (int): width to resize images to after they are read from disk
            batch_size (int): size of batches of data
            model_path (str): path to trained model
            num_classes (int): number of classes in dataset
            epochs (int): number of training epochs
        """
        if model_path is None:
            self.ds = Dataset(
                data_dir, val_split, seed, img_height, img_width, batch_size
            )
            self.num_classes = num_classes
            self.epochs = epochs

            self._create_model()
            self._compile_model()
            self._train_model()
        else:
            self.model = keras.models.load_model(model_path)

    def _create_model(self) -> None:
        self.model = Sequential(
            [
                layers.experimental.preprocessing.Rescaling(
                    1.0 / 255, input_shape=(self.ds.img_height, self.ds.img_width, 3)
                ),
                layers.Conv2D(16, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(32, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(64, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Flatten(),
                layers.Dense(128, activation="relu"),
                layers.Dense(self.num_classes),
            ]
        )

    def _compile_model(self) -> None:
        self.model.compile(
            optimizer="adam",
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

    def _train_model(self) -> None:
        self.history = self.model.fit(
            self.ds.train_ds, validation_data=self.ds.val_ds, epochs=self.epochs
        )

    def save_model(self, path: str) -> None:
        self.model.save(path, overwrite=True)

    def get_model_summary(self):
        return self.model.summary()

    def predict_img(self, img_array: np.array):
        """
        Predicts to which class belongs given image array.

        Predicted class - either 'with_mask' or 'without_mask' string.
        Confidence - percentage of model's confidence of classification.
        """
        batch = tf.expand_dims(img_array, 0)
        predictions = self.model.predict(batch)
        score = tf.nn.softmax(predictions[0])
        predicted_class = self.class_names[np.argmax(score)]
        confidence = 100 * np.max(score)
        return predicted_class, confidence
