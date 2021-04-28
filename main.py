from face_mask_detector import FaceMaskDetector
from parameters import (
    DATA_DIR,
    SAVE_DIR,
    VAL_SPLIT,
    SEED,
    BATCH_SIZE,
    IMG_WIDTH,
    IMG_HEIGHT,
    NUM_CLASSES,
    EPOCHS,
)

if __name__ == "__main__":
    mask_detector = FaceMaskDetector(
        DATA_DIR,
        VAL_SPLIT,
        SEED,
        IMG_HEIGHT,
        IMG_WIDTH,
        BATCH_SIZE,
        NUM_CLASSES,
        EPOCHS,
    )
    # print(mask_detector.get_model_summary())
