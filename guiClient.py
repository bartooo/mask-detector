from DetectWindow import DetectWindow
import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QApplication,
)
from PyQt5 import uic
from ConfigWindow import ConfigWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./ui/main_window.ui", self)
        self._initUI()
        self.show()

    def _initUI(self):
        self.resize(1280, 720)
        start_button = self._make_start_button()
        config_button = self._make_config_button()

    def _make_start_button(self):
        button = QPushButton(self)
        button.setText("Start")
        button.move(int(self.width()//2 - button.width()//2), 400)
        button.clicked.connect(self._on_start_button_clicked)
        return button

    def _make_config_button(self):
        button = QPushButton(self)
        button.setText("Config")
        button.move(int(self.width()//2 - button.width()//2), 500)
        button.clicked.connect(self._on_config_button_clicked)
        return button

    def _on_start_button_clicked(self):
        self.detect_window = DetectWindow(self, "pc", 8006)
        # self.detect_window = DetectWindow(self, "DESKTOP-HT34P2E", 8006)
        self.detect_window.move(500, 100)
        self.hide()
        self.detect_window.show()

    def _on_config_button_clicked(self):
        # self.detect_window = DetectWindow(self, "pc", 8006)
        self.config_window = ConfigWindow(self)
        self.config_window.move(500, 100)
        self.config_window.show()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    # ex = App("ubuntu", 8007)
    # ex = App("DESKTOP-HT34P2E", 8006)
    sys.exit(app.exec_())
