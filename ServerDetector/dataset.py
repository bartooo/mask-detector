import tensorflow as tf
import pathlib


class Dataset:
    def __init__(
        self,
        data_dir: str,
        val_split: float,
        seed: int,
        img_height: int,
        img_width: int,
        batch_size: int,
    ) -> None:
        """

        Args:
            data_dir (str): address to directory of data files
            val_split (float): percentage of data that will be in validation dataset
            seed (int): random seed for shuffling and transformations
            img_height (int): height to resize images to after they are read from disk
            img_width (int): width to resize images to after they are read from disk
            batch_size (int): size of batches of data
        """
        self._data_dir = pathlib.Path(data_dir)
        self._val_split = val_split
        self._seed = seed
        self._img_height = img_height
        self._img_width = img_width
        self._batch_size = batch_size

        self._create_dataset()
        self._conf_ds_for_performance()

    def _create_dataset(self):
        self._train_ds = self._create_train_ds()
        self._class_names = self.train_ds.class_names
        self._val_ds = self._create_val_ds()

    def _create_train_ds(self):
        """
        `keras.preprocessing` generates a `tf.data.Dataset` from image files in a directory.
        Training dataset will contain 80% of images.
        """
        return tf.keras.preprocessing.image_dataset_from_directory(
            self._data_dir,
            validation_split=self._val_split,
            subset="training",
            seed=self._seed,
            image_size=(self._img_height, self._img_width),
            batch_size=self._batch_size,
        )

    def _create_val_ds(self):
        """
        `keras.preprocessing` generates a `tf.data.Dataset` from image files in a directory.
        Validation dataset will contain 20% of images.
        """
        return tf.keras.preprocessing.image_dataset_from_directory(
            self._data_dir,
            validation_split=self._val_split,
            subset="validation",
            seed=self._seed,
            image_size=(self._img_height, self._img_width),
            batch_size=self._batch_size,
        )

    def _conf_ds_for_performance(self):
        """
        `Dataset.cache()` keeps the images in memory after they're loaded off disk during the first epoch. This will ensure the dataset does not become a bottleneck while training your model.

        `Dataset.prefetch()` overlaps data preprocessing and model execution while training.
        """
        AUTOTUNE = tf.data.AUTOTUNE

        self._train_ds = (
            self._train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        )
        self._val_ds = self._val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    @property
    def train_ds(self):
        return self._train_ds

    @train_ds.setter
    def train_ds(self, value):
        self._train_ds = value

    @property
    def val_ds(self):
        return self._val_ds

    @val_ds.setter
    def val_ds(self, value):
        self._val_ds = value

    @property
    def class_names(self):
        return self._class_names

    @class_names.setter
    def class_names(self, value):
        self._class_names = value

    @property
    def img_height(self):
        return self._img_height

    @img_height.setter
    def img_height(self, value):
        self._img_height = value

    @property
    def img_width(self):
        return self._img_width

    @img_width.setter
    def img_width(self, value):
        self._img_width = value
