from pytest import raises
from HostClient import HostClient
import ConnectionExceptions as con_exc


def test_port():
    with raises(con_exc.WrongPortException):
        servDetector = HostClient("whatever", "noint")
    with raises(con_exc.WrongPortException):
        servDetector = HostClient("whatever", 123456)
