import cv2
import numpy as np
import sys
from DetectorExceptions.DataExceptions import validate_datapacker_params


class DataPacker(object):
    def __init__(self, frame: np.ndarray, decision: str, percentage: float):
        """DataPacker construtor.

        Args:
            frame (np.ndarray): Frame to send.
            decision (str): Decision which has been taken by classifier.
            percentage (float): Success of classify by percentage.
        """
        validate_datapacker_params(frame, decision, percentage)
        self._frame = frame
        self._decision = decision
        self._percentage = percentage

    @property
    def frame(self) -> np.ndarray:
        """Frame getter.

        Returns:
            np.ndarray: Object's frame.
        """
        return self._frame

    @property
    def decision(self) -> str:
        """Decision getter.

        Returns:
            str: Object's decision.
        """
        return self._decision

    @property
    def percentage(self) -> float:
        """Percentage getter.

        Returns:
            float: Object's percentage.
        """
        return self._percentage
