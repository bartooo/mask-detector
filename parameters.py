import tensorflow as tf

DATA_DIR = ""  # temporarily needs to be set locally
SAVE_DIR = "./model"
VAL_SPLIT = 0.2
SEED = 123
BATCH_SIZE = 32
IMG_WIDTH = 400
IMG_HEIGHT = 400
AUTOTUNE = tf.data.AUTOTUNE
CLASS_NAMES = ["with_mask", "without_mask"]
EPOCHS = 15
FACE_DETECTOR_PATH = "./haar-classifier/haarcascade_frontalface_default.xml"
SCALE_FACTOR = 1.05
MIN_NEIGHBORS = 13
MIN_SIZE = (10, 10)
COLOR_DICT = {"with_mask": (0, 255, 0), "without_mask": (255, 0, 0)}
