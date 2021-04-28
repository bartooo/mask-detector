from logging import StreamHandler
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
from dataset import Dataset

# TODO: Visualize training results
# TODO: Change loading of data


class FaceMaskDetector:
    def __init__(
        self,
        data_dir: str,
        val_split: float,
        seed: int,
        img_height: int,
        img_width: int,
        batch_size: int,
        num_classes: int = None,
        epochs: int = None,
        model_path: str = None,
    ) -> None:
        """

        Args:
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

    def _create_model(self):
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

    def _compile_model(self):
        self.model.compile(
            optimizer="adam",
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

    def _train_model(self):
        self.history = self.model.fit(
            self.ds.train_ds, validation_data=self.ds.val_ds, epochs=self.epochs
        )

    def save_model(self, path: str):
        self.model.save(path, overwrite=True)

    def get_model_summary(self):
        return self.model.summary()

    def predict_img(self, img_array):
        batch = tf.expand_dims(img_array, 0)
        predictions = self.model.predict(batch)
        score = tf.nn.softmax(predictions[0])
        predicted_class = self.class_names[np.argmax(score)]
        confidence = 100 * np.max(score)
        return predicted_class, confidence
