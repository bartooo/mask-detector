"""Script helps carrying out teaching mask-detecting model.
"""
import cv2
from ServerDetector.face_mask_detector import FaceMaskDetector
from ServerDetector.dataset import Dataset
from ServerDetector.parameters import (
    DATA_DIR,
    FACE_DETECTOR_PATH,
    SAVE_DIR,
    VAL_SPLIT,
    SEED,
    BATCH_SIZE,
    IMG_WIDTH,
    IMG_HEIGHT,
    FACE_DETECTOR_PATH,
)

if __name__ == "__main__":
    # ds = Dataset(DATA_DIR, VAL_SPLIT, SEED, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE)
    # mask_detector = FaceMaskDetector(face_detector_path=FACE_DETECTOR_PATH, ds=ds)
    # mask_detector.create()
    # mask_detector.save_model(SAVE_DIR)
    pass
