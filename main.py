import cv2
from face_mask_detector import FaceMaskDetector
from dataset import Dataset
from parameters import (
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


def main():
    test_img = cv2.imread("./images/man_with_mask.jpg")
    test_img = cv2.resize(test_img, (IMG_WIDTH, IMG_HEIGHT))
    mask_detector = FaceMaskDetector(
        face_detector_path=FACE_DETECTOR_PATH, model_path=SAVE_DIR
    )
    predicted_class, confidence, res = mask_detector.predict_img(test_img)
    print(
        f"Image classified to: {predicted_class} with confidence of {confidence:.2f}%"
    )
    cv2.imshow("result image", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    ds = Dataset(DATA_DIR, VAL_SPLIT, SEED, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE)
    mask_detector = FaceMaskDetector(face_detector_path=FACE_DETECTOR_PATH, ds=ds)
    mask_detector.create()
    # mask_detector.save_model(SAVE_DIR)

    # main()
