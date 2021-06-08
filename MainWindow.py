from DetectWindow import DetectWindow
import sys
from PyQt5.QtWidgets import (
    QDialog,
    QMainWindow,
    QPushButton,
    QApplication,
)
from PyQt5 import QtCore, QtGui, uic
from ConfWindow import ConfWindow
from backports import configparser
from MainWindowUI import Ui_MainWindow
from PyQt5.Qt import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import socket


def get_logging_param(comm_args):
    if len(comm_args) == 1:
        return False
    elif len(comm_args) == 2 and comm_args[1] == "--logging":
        return True
    else:
        raise Exception(
            "Only possible argument to pass (not required) is: --logging which enables logging"
        )


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, logging_enabled, parent=None):
        super().__init__(parent)
        self.logging_enabled = logging_enabled
        self.setupUi(self)
        self._config_path = "ClientDetector/config.ini"
        self._setup_cursors()
        self._setup_logo()
        self._load_config()
        self._connect_buttons()
        self.show()

    def _setup_logo(self):
        loaded_pixmap = QPixmap("ui/logo-gold.png").scaled(600, 600, Qt.KeepAspectRatio)
        self.setWindowIcon(QtGui.QIcon("ui/logo.png"))
        self.logo_label.setPixmap(loaded_pixmap)

    def _setup_cursors(self):
        self.button_config.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_run_detector.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def _load_config(self):
        cfg_parser = configparser.ConfigParser()
        cfg_parser.read(self._config_path)
        self.server_name = cfg_parser.get("DEFAULT", "ServerName")
        self.server_port = int(cfg_parser.get("DEFAULT", "ServerPort"))

    def _connect_buttons(self):
        self.button_config.clicked.connect(self._on_config_button_clicked)
        self.button_run_detector.clicked.connect(self._on_start_button_clicked)

    def _on_start_button_clicked(self):
        self.detect_window = None
        try:
            self.detect_window = DetectWindow(self, self.logging_enabled)
            self.detect_window.move(500, 100)
            self.hide()
            self.detect_window.show()
            self.warning_label.clear()
            self.warning_label.setProperty("is_hidden", "true")
            self.warning_label.style().unpolish(self.warning_label)
            self.warning_label.style().polish(self.warning_label)
            self.warning_label.update()
        except (socket.gaierror, ConnectionRefusedError) as e:
            self.warning_label.setText("SETUP YOUR CONNECTION BEFORE STARTING PROGRAM!")
            self.warning_label.setProperty("is_hidden", "false")
            self.warning_label.style().unpolish(self.warning_label)
            self.warning_label.style().polish(self.warning_label)
            self.warning_label.update()

    def _on_config_button_clicked(self):
        self.config_window = ConfWindow(self)
        self.config_window.show()
