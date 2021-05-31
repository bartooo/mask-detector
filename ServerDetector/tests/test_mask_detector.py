import pytest

from ServerDetector.face_mask_detector import FaceMaskDetector
from ServerDetector.parameters import FACE_DETECTOR_PATH, SAVE_DIR, IMG_HEIGHT, IMG_WIDTH
import cv2

mask_detector = FaceMaskDetector(
    face_detector_path=FACE_DETECTOR_PATH, model_path=SAVE_DIR
)


@pytest.mark.parametrize(
    "test_img_path, expected",
    [
        ("./ServerDetector/images/man_with_mask.jpg", "with_mask"),
        ("./ServerDetector/images/man_with_maskv2.jpg", "with_mask"),
        ("./ServerDetector/images/woman_with_mask.jpg", "with_mask"),
        ("./ServerDetector/images/woman_with_maskv2.jpg", "with_mask"),
        ("./ServerDetector/images/woman_with_maskv3.jpg", "with_mask"),
        ("./ServerDetector/images/woman_with_maskv4.jpg", "with_mask"),
        ("./ServerDetector/images/messi.jpg", "without_mask"),
        ("./ServerDetector/images/ronaldo.jpg", "without_mask"),
        ("./ServerDetector/images/radcliffe_without_mask.jpg", "without_mask"),
        ("./ServerDetector/images/watson_without_mask.jpg", "without_mask"),
        ("./ServerDetector/images/ed_without_mask.jpg", "without_mask"),
        ("./ServerDetector/images/popek_without_mask.jpg", "without_mask"),
    ],
)
def test_model(test_img_path, expected):
    test_img = cv2.imread(test_img_path)
    test_img = cv2.resize(test_img, (IMG_WIDTH, IMG_HEIGHT))
    predicted_class, _, _ = mask_detector.predict_img(test_img)
    assert predicted_class == expected
