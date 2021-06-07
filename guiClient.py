from DetectWindow import DetectWindow
import sys
from PyQt5.QtWidgets import (
    QDialog,
    QMainWindow,
    QPushButton,
    QApplication,
)
from PyQt5 import uic
from ConfWindow import ConfWindow
from backports import configparser


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        super(QDialog, self).__init__()
        self.config_path = "ClientDetector/config.ini"
        self.load_config()
        self._initUI()
        self.show()

    def load_config(self):
        cfg_parser = configparser.ConfigParser()
        cfg_parser.read(self.config_path)
        self.server_name = cfg_parser.get("DEFAULT", "ServerName")
        self.server_port = int(cfg_parser.get("DEFAULT", "ServerPort"))

    def _initUI(self):
        self.resize(1280, 720)
        start_button = self._make_start_button()
        config_button = self._make_config_button()

    def _make_start_button(self):
        button = QPushButton(self)
        button.setText("Start")
        button.move(int(self.width() // 2 - button.width() // 2), 400)
        button.clicked.connect(self._on_start_button_clicked)
        return button

    def _make_config_button(self):
        button = QPushButton(self)
        button.setText("Config")
        button.move(int(self.width() // 2 - button.width() // 2), 500)
        button.clicked.connect(self._on_config_button_clicked)
        return button

    def _on_start_button_clicked(self):
        self.detect_window = DetectWindow(self)
        self.detect_window.move(500, 100)
        self.hide()
        self.detect_window.show()

    def _on_config_button_clicked(self):
        self.config_window = ConfWindow(self)
        self.config_window.show()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
