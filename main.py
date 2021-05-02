import PIL
from matplotlib import pyplot as plt
from face_mask_detector import FaceMaskDetector
from parameters import (
    DATA_DIR,
    SAVE_DIR,
    VAL_SPLIT,
    SEED,
    BATCH_SIZE,
    IMG_WIDTH,
    IMG_HEIGHT,
    CLASS_NAMES,
    EPOCHS,
)


def main():
    img = PIL.Image.open("./images/me_with_paper_mask.jpg")
    img = img.resize((IMG_WIDTH, IMG_HEIGHT))
    img = img.rotate(90)
    img.show()
    mask_detector = FaceMaskDetector(class_names=CLASS_NAMES, model_path=SAVE_DIR)
    predicted_class, confidence = mask_detector.predict_img(img)
    print(
        f"Image classified to: {predicted_class} with confidence of {confidence:.2f}%"
    )


if __name__ == "__main__":
    """
    mask_detector = FaceMaskDetector(
        class_names=CLASS_NAMES,
        model_path=None,
        data_dir=DATA_DIR,
        val_split=VAL_SPLIT,
        seed=SEED,
        img_height=IMG_HEIGHT,
        img_width=IMG_WIDTH,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
    )
    mask_detector.save_model(SAVE_DIR)
    """
    main()
