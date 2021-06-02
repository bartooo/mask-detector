from pytest import raises
import sys
from ClientDetector.HostClient import HostClient
import DetectorExceptions.ConnectionExceptions as con_exc


def test_port():
    with raises(con_exc.WrongPortException):
        servDetector = HostClient("whatever", "noint")
    with raises(con_exc.WrongPortException):
        servDetector = HostClient("whatever", 123456)
