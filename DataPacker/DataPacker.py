import cv2
import numpy as np
import sys
from DetectorExceptions.DataExceptions import validate_datapacker_params
import datetime


class DataPacker(object):
    def __init__(
        self,
        frame: np.ndarray,
        decision: str,
        percentage: float,
        time_sended: datetime.time = None,
    ):
        """DataPacker construtor.

        Args:
            frame (np.ndarray): Frame to send.
            decision (str): Decision which has been taken by classifier.
            percentage (float): Success of classify by percentage.
            time_sended (datetime.time): Time in which picture has been taken
        """
        validate_datapacker_params(frame, decision, percentage, time_sended)
        self._frame = frame
        self._decision = decision
        self._percentage = percentage
        self._time_sended = (
            datetime.datetime.now() if time_sended is None else time_sended
        )

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

    @property
    def time_sended(self) -> datetime.time:
        """Time of picture getter.

        Returns:
            datetime.time: Time at which picture has been taken.
        """
        return self._time_sended
