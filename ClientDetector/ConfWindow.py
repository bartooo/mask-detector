from PyQt5.QtWidgets import QDialog, QMainWindow, QDesktopWidget
from ClientDetector.pyui.ConfigWindowUI import Ui_ConfigureDialog
from PyQt5 import Qt, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSignal, QThread, pyqtSlot, QObject, QEvent
import socket
import struct
import pickle
import typing
from PyQt5.Qt import QImage, QObject, QPixmap
import cv2
from backports import configparser
from ClientDetector.DataGetter import DataGetter


class ButtonThread(QThread):
    """Class represents thread for checking connection with server."""

    def __init__(self, parent: typing.Optional[QObject]) -> None:
        """ButtonThread constructor.

        Args:
            parent (typing.Optional[QObject]): parent QObject
        """
        super().__init__(parent=parent)
        self.server_name = parent.server_name
        self.server_port = parent.server_port
        self.data_getter = DataGetter()

    change_photo_label_text = pyqtSignal(str)
    change_photo_label_img = pyqtSignal(QImage)
    change_latency_label = pyqtSignal(str)
    client_socket = None

    def run(self) -> None:
        """Function responsible for running thread."""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.server_name, self.server_port))
            for _ in range(2):
                data_recv_pickled = self.data_getter.get(self.client_socket)
            # unpickle what we got
            data_recv = pickle.loads(data_recv_pickled)
            rgbImage = cv2.cvtColor(data_recv.frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(
                rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888
            )
            self.change_photo_label_text.emit("")
            self.change_photo_label_img.emit(
                convertToQtFormat.scaled(350, 350, QtCore.Qt.KeepAspectRatio)
            )
            self.change_latency_label.emit(
                f"{data_recv.time_sended.total_seconds()*1000:.3f} ms"
            )
            self.client_socket.close()
        except (ConnectionRefusedError, socket.gaierror, struct.error) as conn_exc:
            self.change_photo_label_text.emit("CONNECTION\nREFUSED!")
            self.change_latency_label.emit("N/A!")
            self.client_socket.close()


class ConfWindow(QDialog, Ui_ConfigureDialog):
    """Class represents Config Window in GUI."""

    def __init__(self, parent: QObject = None) -> None:
        """Config Window constructor.

        Args:
            parent (QObject, optional): parent of object, defaults to None
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.Popup
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
        )
        self.center()
        self.position = self.pos()
        self.setup_cursors()
        self.setup_buttons()
        self.server_name = self.parent().server_name
        self.server_port = self.parent().server_port

    @pyqtSlot(QImage)
    def set_image(self, image: QImage) -> None:
        """Image setter on photo label.

        Args:
            image ([type]): [description]
        """
        self.photo_label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str)
    def set_latency_label(self, text: str) -> None:
        """Function sets info in latency label.

        Args:
            text (str): latency to set
        """
        self.latency_out_label.setText(text)

    @pyqtSlot(str)
    def set_image_label_text(self, text: str) -> None:
        """Function sets text on image label.

        Args:
            text (str): text to set
        """
        self.photo_label.autoFillBackground()
        self.photo_label.setText(text)

    def keyPressEvent(self, event: QEvent) -> None:
        """Function handles that user cant exit window with escape.

        Args:
            event ([type]): [description]
        """
        if event.key() == QtCore.Qt.Key_Escape:
            event.ignore()
        else:
            event.accept()

    def center(self) -> None:
        """Function centers window."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event: QEvent) -> None:
        """Function overrides pressing on window by setting oldPos.

        Args:
            event (QEvent): event to be overriden
        """
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event: QEvent) -> None:
        """Function moves window with cursor.

        Args:
            event (QEvent): event to overriden
        """
        if (
            self.x() <= event.globalPos().x() <= self.x() + self.width()
            and self.y() <= event.globalPos().y() <= self.y() + self.height()
        ):
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def setup_cursors(self) -> None:
        """Function setup cursors on each button."""
        self.test_connection_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.change_server_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.server_box.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def setup_buttons(self) -> None:
        """Function assigns functions to clicked actions."""
        self.test_connection_button.clicked.connect(self.on_test_connection_clicked)
        self.change_server_button.clicked.connect(self.on_change_server_clicked)
        self.server_box.setCurrentText(self.parent().server_name)
        self.exit_button.clicked.connect(self.on_exit_button_clicked)

    def on_test_connection_clicked(self) -> None:
        """Funtion runs thread when test_connection button is clicked."""
        self.server_name = self.server_box.currentText()
        th = ButtonThread(self)
        th.change_latency_label.connect(self.set_latency_label)
        th.change_photo_label_img.connect(self.set_image)
        th.change_photo_label_text.connect(self.set_image_label_text)
        th.run()

    def on_change_server_clicked(self) -> None:
        """Function changes server and overrides config.ini file."""
        self.parent().server_name = self.server_box.currentText()
        self.server_name = self.parent().server_name
        cfg_parser = configparser.ConfigParser()
        cfg_parser.read(self.parent()._config_path)
        cfg_parser["DEFAULT"]["servername"] = self.server_box.currentText()
        with open(self.parent()._config_path, "w+") as configfile:
            cfg_parser.write(configfile)

    def on_exit_button_clicked(self) -> None:
        """Closing window when clicked on exit button."""
        self.close()
