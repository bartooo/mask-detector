from typing import Any
import numpy as np

MAX_DECISION_LENGTH = 1000

class DataPackerException(Exception):
    """Raised when DataPacker initialization faced an error. 
    """


def validate_frame(frame: Any) -> None:
    """Function validates frame.

    Args:
        frame (Any): Frame to validate.

    Raises:
        DataPackerException: When frame has wrong type or doesnt have positive shape.
    """
    if type(frame) != np.ndarray:
        raise DataPackerException("Wrong type of frame! Should be np.ndarray!")
    elif frame.shape[0] <=0 or frame.shape[1] <=0:
        raise DataPackerException("Error while getting frame - shapes shouldnt be <=0!")


def validate_percentage(percentage: Any) -> None:
    """Function validates percentage.

    Args:
        percentage (Any): Given percentage to validate.

    Raises:
        DataPackerException: When percentage has incorrect type or wrong range.
    """
    if type(percentage) != float and type(percentage) != int:
        raise DataPackerException("Wrong type of percentage! Should be float/int!")
    else:
        if percentage < 0 or percentage > 100:
            raise DataPackerException("Percentage should be a number between 0 and 100!")


def validate_decision(decision: Any) -> None:
    """Funcion validates decision.

    Args:
        decision (Any): decision to validate.

    Raises:
        DataPackerException: When decision is wrong type or has incorrect length.
    """
    if type(decision) != str:
        raise DataPackerException("Wrong type of decision! Should be str!")
    elif len(decision) <= 0 or len(decision) >= MAX_DECISION_LENGTH:
        raise DataPackerException(f"Wrong length of decision! Should be between 0 and {MAX_DECISION_LENGTH}!")


def validate_datapacker_params(frame: Any, decision: Any, percentage: Any) -> None:
    """Validates DataPacker parameters.

    Args:
        frame (Any): Frame to validate.
        percentage (Any): Percentage to validate.
        decision (Any): Decision to validate.
    """
    validate_frame(frame)
    validate_decision(decision)
    validate_percentage(percentage)