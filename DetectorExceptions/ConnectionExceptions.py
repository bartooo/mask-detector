from typing import Any


class WrongPortException(Exception):
    """Raised when wrong port is given (should be 4-digit int)."""

    pass


def validate_port(given_port: Any):
    if type(given_port) != int:
        raise WrongPortException("Port should be an integer!")
    port_str = str(given_port)
    if len(port_str) != 4:
        raise WrongPortException("Port should be 4-digit!")
