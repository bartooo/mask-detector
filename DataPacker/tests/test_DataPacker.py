import pytest
from DataPacker.DataPacker import DataPacker
import cv2
import numpy as np
import DetectorExceptions.DataExceptions as d_exc
import datetime


def test_getters():
    correct_image = cv2.imread(
        "./ServerDetector/tests/img_for_datapacker_test.jpg", cv2.IMREAD_UNCHANGED
    )
    correct_percentage = 70.2
    correct_decision = "No mask!"
    dataPacker = DataPacker(correct_image, correct_decision, correct_percentage)
    assert dataPacker.decision == correct_decision
    assert dataPacker.percentage == correct_percentage
    loaded_image = dataPacker.frame
    assert correct_image.shape == loaded_image.shape
    difference = cv2.subtract(correct_image, loaded_image)
    b, g, r = cv2.split(difference)
    assert (
        cv2.countNonZero(b) == 0
        and cv2.countNonZero(g) == 0
        and cv2.countNonZero(r) == 0
    )
    assert type(dataPacker.time_sended) == datetime.datetime


def test_validation():
    correct_image = cv2.imread(
        "./ServerDetector/tests/img_for_datapacker_test.jpg", cv2.IMREAD_UNCHANGED
    )
    correct_percentage = 70.2
    correct_decision = "No mask!"
    wrong_image = np.ndarray((0, 0))
    wrong_percentage1 = "wrong_percentage"
    wrong_percentage2 = -123
    wrong_percentage3 = 123
    wrong_decision1 = ""
    wrong_decision2 = 2115
    with pytest.raises(d_exc.DataPackerException):
        dataPacker = DataPacker(wrong_image, wrong_decision1, wrong_percentage1)

    with pytest.raises(d_exc.DataPackerException):
        dataPacker = DataPacker(correct_image, wrong_decision1, wrong_percentage1)

    with pytest.raises(d_exc.DataPackerException):
        dataPacker = DataPacker(correct_image, wrong_decision2, wrong_percentage1)

    with pytest.raises(d_exc.DataPackerException):
        dataPacker = DataPacker(correct_image, correct_decision, wrong_percentage1)

    with pytest.raises(d_exc.DataPackerException):
        dataPacker = DataPacker(correct_image, correct_decision, wrong_percentage2)

    with pytest.raises(d_exc.DataPackerException):
        dataPacker = DataPacker(correct_image, correct_decision, wrong_percentage3)
