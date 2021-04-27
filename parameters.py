import tensorflow as tf

DATA_DIR = "C:\\Users\\bartosz\\Desktop\\data"
SAVE_DIR = "./model"
VAL_SPLIT = 0.2
SEED = 123
BATCH_SIZE = 32
IMG_WIDTH = 180
IMG_HEIGHT = 180
AUTOTUNE = tf.data.AUTOTUNE
NUM_CLASSES = 2
EPOCHS = 5
