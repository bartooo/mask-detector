from ClientDetector.DetectWindow import DetectWindow
import sys
from PyQt5.QtWidgets import (
    QDialog,
    QMainWindow,
    QPushButton,
    QApplication,
    QLabel,
)
from PyQt5 import QtCore, QtGui, uic
from ClientDetector.ConfWindow import ConfWindow
from backports import configparser
from ClientDetector.pyui.MainWindowUI import Ui_MainWindow
from PyQt5.Qt import QPixmap
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QCursor
import socket


def get_logging_param(comm_args: list) -> bool:
    """Function handles passing parameters for program (from console).

    Args:
        comm_args (list): list of system command line args while running program

    Raises:
        Exception: When user passes other argument than empty or '--logging'.

    Returns:
        bool: true if logging param is set
    """
    if len(comm_args) == 1:
        return False
    elif len(comm_args) == 2 and comm_args[1] == "--logging":
        return True
    else:
        raise Exception(
            "Only possible argument to pass (not required) is: --logging which enables logging"
        )


class MainWindow(QMainWindow, Ui_MainWindow):
    """Class represents Main Window of GUI.\
    """

    def __init__(self, logging_enabled: bool, parent: QObject = None) -> None:
        """MainWindow constructor.

        Args:
            logging_enabled (bool): tells if logging is enabled.
            parent (QObject, optional): reference to parent widget, defaults to None
        """
        super().__init__(parent)
        self.logging_enabled = logging_enabled
        self.setupUi(self)
        self._config_path = "ClientDetector/config.ini"
        self._setup_cursors()
        self._setup_logo()
        self._load_config()
        self._connect_buttons()
        self.show()

    def _setup_logo(self) -> None:
        """Functions setup window logo and main logo."""
        loaded_pixmap = QPixmap("ClientDetector/resources/logo-gold.png").scaled(
            600, 600, Qt.KeepAspectRatio
        )
        self.setWindowIcon(QtGui.QIcon("ClientDetector/resources/logo.png"))
        self.logo_label.setPixmap(loaded_pixmap)

    def _setup_cursors(self) -> None:
        """Funtion setup cursors on buttons."""
        self.button_config.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_run_detector.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def _load_config(self) -> None:
        """Function load server name and server port from .ini file."""
        cfg_parser = configparser.ConfigParser()
        cfg_parser.read(self._config_path)
        self.server_name = cfg_parser.get("DEFAULT", "ServerName")
        self.server_port = int(cfg_parser.get("DEFAULT", "ServerPort"))

    def _connect_buttons(self) -> None:
        """Function assings proper methods to clicking on buttons."""
        self.button_config.clicked.connect(self._on_config_button_clicked)
        self.button_run_detector.clicked.connect(self._on_start_button_clicked)

    def _on_start_button_clicked(self) -> None:
        """Function starts DetectWindow if there is connection, else shows warning."""
        self.detect_window = None
        try:
            self.detect_window = DetectWindow(self, self.logging_enabled)
            self.detect_window.move(500, 100)
            self.hide()
            self.detect_window.show()
            self.warning_label.clear()
            self._change_label_property(self.warning_label, "is_hidden", "true")
        except (socket.gaierror, ConnectionRefusedError) as e:
            self.warning_label.setText("SETUP YOUR CONNECTION BEFORE STARTING PROGRAM!")
            self._change_label_property(self.warning_label, "is_hidden", "false")

    def _change_label_property(
        self, label: QLabel, property_name: str, property_value: str
    ) -> None:
        """Function changes label property and resets it - allows it to change stylesheet of label dynamically.

        Args:
            label (QLabel): label for which property is being changed
            property_name (str): name of property to change
            property_value (str): value of property to change
        """
        label.setProperty(property_name, property_value)
        label.style().unpolish(label)
        label.style().polish(label)
        label.update()

    def _on_config_button_clicked(self) -> None:
        """Function runs ConfigWindow."""
        self.config_window = ConfWindow(self)
        self.config_window.show()
