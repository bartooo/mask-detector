import socket
import typing
import cv2
import pickle
import struct
import sys
import datetime
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QApplication
from PyQt5.QtCore import QObject, QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5 import uic
from DetectorExceptions.ConnectionExceptions import WrongPortException, validate_port
from DataPacker.DataPacker import DataPacker


class Thread(QThread):
    
    def __init__(self, parent: typing.Optional[QObject]) -> None:
        super().__init__(parent=parent)
        self._finish = False
    
    changePixmap = pyqtSignal(QImage)
    changeLabel2Text = pyqtSignal(str)
    changeLabel3Text = pyqtSignal(str)
    changeLabel4Text = pyqtSignal(str)
    server_name = None
    server_port = None
    client_socket = None



    def run(self):
        payload_size = struct.calcsize("Q")
        data = b""
        while True:
            # while loop to get size of receiving data
            while len(data) < payload_size:
                packet = self.client_socket.recv(4 * 1024)  # 4KB
                if not packet:
                    break
                data += packet
            # counting size of sending data
            packed_msg_size = data[:payload_size]
            print(len(packed_msg_size))
            # if in first while loop there was download part of data, need to add it on start
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            # receiving concrete data
            while len(data) < msg_size:
                data += self.client_socket.recv(4 * 1024)
            # getting all data for current state
            data_recv_pickled = data[:msg_size]
            # setting data to whats left for next state
            data = data[msg_size:]
            # unpickle what we got
            data_recv = pickle.loads(data_recv_pickled)
            # show image and if q pressed - stop
            print(
                # f"[CLIENT] GOT IMAGE AT TIME: {data_recv.decision} | WITH PERCENTAGE: {data_recv.percentage}% | NOW: {datetime.datetime.now()} | SEND: {data_recv.time_sended}"
                f"[CLIENT] GOT IMAGE AT TIME: {data_recv.decision} | WITH PERCENTAGE: {data_recv.percentage}% | DIFF: {data_recv.time_sended}"
            )
            rgbImage = cv2.cvtColor(data_recv.frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(
                rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888
            )
            p = convertToQtFormat.scaled(600, 600, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
            self.changeLabel2Text.emit(f"Prediction: {data_recv.percentage:.3f}%")
            self.changeLabel3Text.emit(
                # f"Delay: {(datetime.datetime.now() - data_recv.time_sended).total_seconds() * 1000:.3f} ms"
                f"Delay: {data_recv.time_sended} ms"
            )
            self.changeLabel4Text.emit(f"Decision: {data_recv.decision}")



class DetectWindow(QWidget):
    def __init__(self, serv_name: str, serv_port: int):
        super().__init__()
        self.title = "Hello"
        self.left = 0
        self.width = 0
        self.top = 0
        self.height = 0
        validate_port(serv_port)
        self.server_name = serv_name
        self.server_port = serv_port
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str)
    def setLabel2Text(self, text):
        self.label2.setText(text)

    @pyqtSlot(str)
    def setLabel3Text(self, text):
        self.label3.setText(text)

    @pyqtSlot(str)
    def setLabel4Text(self, text):
        self.label4.setText(text)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(600, 740)

        # create a label
        self.label = QLabel(self)
        self.label.move(0, 0)
        self.label.resize(600, 600)
        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Arial", 20))
        self.label2.move(0, 650)
        self.label2.resize(600, 140)
        self.label2.setText("Prediction: ")
        self.label3 = QLabel(self)
        self.label3.setFont(QFont("Arial", 20))
        self.label3.move(0, 600)
        self.label3.resize(600, 140)
        self.label3.setText("Latency: ")
        self.label4 = QLabel(self)
        self.label4.setFont(QFont("Arial", 20))
        self.label4.move(0, 550)
        self.label4.resize(600, 140)
        self.label4.setText("Decision: ")
        
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.changeLabel2Text.connect(self.setLabel2Text)
        th.changeLabel3Text.connect(self.setLabel3Text)
        th.changeLabel4Text.connect(self.setLabel4Text)
        th.server_name = self.server_name
        th.server_port = self.server_port
        th.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        th.client_socket.connect((self.server_name, self.server_port))
        th.start()


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./ui/main_window.ui", self)
        self._initUI()
        self.show()

    def _initUI(self):
        start_button = self._make_start_button()

    def _make_start_button(self):
        button = QPushButton(self)
        button.setText("Start")
        button.move(400, 450)
        button.clicked.connect(self._on_start_button_clicked)
        return button

    def _on_start_button_clicked(self):
        self.detect_window = DetectWindow("pc", 8006)
        self.hide()
        self.detect_window.move(500, 100)
        self.detect_window.show()

if __name__ == "__main__":
    
    app = QApplication([])
    app.setApplicationName("Poka sowe")
    window = MainWindow()
    # ex = App("ubuntu", 8007)
    #ex = App("DESKTOP-HT34P2E", 8006)
    sys.exit(app.exec_())
