import pytest
from face_mask_detector import FaceMaskDetector
from parameters import FACE_DETECTOR_PATH, SAVE_DIR, IMG_HEIGHT, IMG_WIDTH
import cv2
import os

# mask_detector = FaceMaskDetector(
#     face_detector_path=FACE_DETECTOR_PATH, model_path=SAVE_DIR
# )
mask_detector = FaceMaskDetector(
    face_detector_path=os.path.abspath(os.getcwd())+"/haar-classifier/haarcascade_frontalface_default.xml", model_path=os.path.abspath(os.getcwd())+"/model/"
)
images_path = os.path.abspath(os.getcwd()) + "/images/"

@pytest.mark.parametrize(
    "test_img_path, expected",
    [
        (images_path+"man_with_mask.jpg", "with_mask"),
        (images_path+"man_with_maskv2.jpg", "with_mask"),
        (images_path+"woman_with_mask.jpg", "with_mask"),
        (images_path+"woman_with_maskv2.jpg", "with_mask"),
        (images_path+"woman_with_maskv3.jpg", "with_mask"),
        (images_path+"woman_with_maskv4.jpg", "with_mask"),
        (images_path+"messi.jpg", "without_mask"),
        (images_path+"ronaldo.jpg", "without_mask"),
        (images_path+"radcliffe_without_mask.jpg", "without_mask"),
        (images_path+"watson_without_mask.jpg", "without_mask"),
        (images_path+"ed_without_mask.jpg", "without_mask"),
        (images_path+"popek_without_mask.jpg", "without_mask"),
    ],
)
def test_model(test_img_path, expected):
    test_img = cv2.imread(test_img_path)
    test_img = cv2.resize(test_img, (IMG_WIDTH, IMG_HEIGHT))
    predicted_class, _, _ = mask_detector.predict_img(test_img)
    assert predicted_class == expected
