import tensorflow as tf
import pathlib
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# TODO: Visualize training results
# TODO: Change loading of data


class FaceMaskDetector:
    def __init__(
        self,
        model_path: str = None,
        data_dir: str = None,
        val_split: float = None,
        seed: int = None,
        img_height: int = None,
        img_width: int = None,
        batch_size: int = None,
        num_classes: int = None,
        epochs: int = None,
    ) -> None:
        """

        Args:
            data_dir (str): address to directory of data files
            val_split (float): percentage of data that will be in validation dataset
            seed (int): random seed for shuffling and transformations
            img_height (int): height to resize images to after they are read from disk
            img_width (int): width to resize images to after they are read from disk
            batch_size (int): size of batches of data
            num_classes (int): number of classes in dataset
            epochs (int): number of training epochs
        """
        if model_path is None:
            self.data_dir = pathlib.Path(data_dir)
            self.val_split = val_split
            self.seed = seed
            self.img_height = img_height
            self.img_width = img_width
            self.batch_size = batch_size
            self.num_classes = num_classes
            self.epochs = epochs

            self._create_dataset()
            self._conf_ds_for_performance()
            self._create_model()
            self._compile_model()
            self._train_model()
        else:
            self.model = keras.models.load_model(model_path)

    def _create_dataset(self):
        self.train_ds = self._create_train_ds()
        self.val_ds = self._create_val_ds()

    def _create_train_ds(self):
        """
        `keras.preprocessing` generates a `tf.data.Dataset` from image files in a directory.
        Training dataset will contain 80% of images.
        """
        return tf.keras.preprocessing.image_dataset_from_directory(
            self.data_dir,
            validation_split=self.val_split,
            subset="training",
            seed=self.seed,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size,
        )

    def _create_val_ds(self):
        """
        `keras.preprocessing` generates a `tf.data.Dataset` from image files in a directory.
        Validation dataset will contain 20% of images.
        """
        return tf.keras.preprocessing.image_dataset_from_directory(
            self.data_dir,
            validation_split=self.val_split,
            subset="validation",
            seed=self.seed,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size,
        )

    def _conf_ds_for_performance(self):
        """
        `Dataset.cache()` keeps the images in memory after they're loaded off disk during the first epoch. This will ensure the dataset does not become a bottleneck while training your model.

        `Dataset.prefetch()` overlaps data preprocessing and model execution while training.
        """
        AUTOTUNE = tf.data.AUTOTUNE

        self.train_ds = (
            self.train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        )
        self.val_ds = self.val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    def _create_model(self):
        self.model = Sequential(
            [
                layers.experimental.preprocessing.Rescaling(
                    1.0 / 255, input_shape=(self.img_height, self.img_width, 3)
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
            self.train_ds, validation_data=self.val_ds, epochs=self.epochs
        )

    def save_model(self, path):
        self.model.save(path, overwrite=True)

    def get_model_summary(self):
        return self.model.summary()
