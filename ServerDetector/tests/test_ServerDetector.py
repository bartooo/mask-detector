from pytest import raises
from ServerDetector.ServerDetector import ServerDetector
import DetectorExceptions.ConnectionExceptions as con_exc


def test_port():
    with raises(con_exc.WrongPortException):
        servDetector = ServerDetector("whatever", "noint")
    with raises(con_exc.WrongPortException):
        servDetector = ServerDetector("whatever", 123456)
