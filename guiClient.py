import socket
import typing
import cv2
import pickle
import struct
import sys
import datetime
from PyQt5.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QApplication,
)
from PyQt5.QtCore import QObject, QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5 import uic
from DetectorExceptions.ConnectionExceptions import WrongPortException, validate_port
from DataPacker.DataPacker import DataPacker
import time
import threading

class Thread(QThread):
    def __init__(self, parent: typing.Optional[QObject]) -> None:
        super().__init__(parent=parent)
        self._finish = False
        self._run_seconds = 0
        self.timer = None

    change_pixmap = pyqtSignal(QImage)
    change_conf_label = pyqtSignal(str)
    change_delay_label = pyqtSignal(str)
    change_pred_label = pyqtSignal(str)
    add_image = pyqtSignal(QImage, str, str, int)
    show_result = pyqtSignal()
    server_name = None
    server_port = None
    client_socket = None
    
    @property
    def run_seconds(self):
        return self._run_seconds

    @run_seconds.setter
    def run_seconds(self, value: bool):
        self._run_seconds = value

    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, value: bool):
        self._finish = value

    def run(self):
        payload_size = struct.calcsize("Q")
        data = b""
        
        while not self.finish and self.run_seconds < 5:
            # while loop to get size of receiving data
            while len(data) < payload_size:
                packet = self.client_socket.recv(4 * 1024)  # 4KB
                if not packet:
                    break
                data += packet
            # counting size of sending data
            packed_msg_size = data[:payload_size]
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
            self.frame = convertToQtFormat.scaled(100, 100, Qt.KeepAspectRatio)
            self.confidence = f"{data_recv.percentage:.3f}"
            self.prediction = f"{data_recv.decision}"
            self.change_pixmap.emit(convertToQtFormat.scaled(300, 300, Qt.KeepAspectRatio))
            self.change_conf_label.emit(f"Confidence: {self.confidence}%")
            self.change_delay_label.emit(
                # f"Delay: {(datetime.datetime.now() - data_recv.time_sended).total_seconds() * 1000:.3f} ms"
                f"Delay: {data_recv.time_sended} ms"
            )
            self.change_pred_label.emit(f"Prediction: {self.prediction}")
            if self.run_seconds == 0:
                self._send_frame()
                
            elif self.run_seconds == 5:
                self.timer.cancel()
                
        self.client_socket.close()
        self.show_result.emit()


    def _send_frame(self):
        self.add_image.emit(self.frame, self.confidence, self.prediction, self.run_seconds)
        self.run_seconds += 1
        self.timer = threading.Timer(1.0, self._send_frame)
        self.timer.start()
        

class DetectWindow(QDialog):
    def __init__(self, parent, serv_name: str, serv_port: int):
        super().__init__(parent=parent)
        self.title = "Hello"
        self.left = 0
        self.width = 0
        self.top = 0
        self.height = 0
        validate_port(serv_port)
        self.server_name = serv_name
        self.server_port = serv_port
        self.images_list = []
        self._initUI()

    
    @pyqtSlot(QImage)
    def set_main_image(self, image):
        self.img_label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str)
    def set_conf_label(self, text):
        self.conf_label.setText(text)

    @pyqtSlot(str)
    def set_delay_label(self, text):
        self.delay_label.setText(text)

    @pyqtSlot(str)
    def set_pred_label(self, text):
        self.pred_label.setText(text)
    
    @pyqtSlot(QImage, str, str, int)
    def add_image(self, image, prediction, confidence, second):
        self.images_list.append((image, prediction, confidence, second))
        self._display_image(self.images_list[len(self.images_list)-1])

    def _display_image(self, image):
        img_label = QLabel(self)
        x_offset = 100 + ((len(self.images_list) - 1) * 150)
        img_label.move(x_offset, 380)
        img_label.resize(100, 100)
        img_label.setPixmap(QPixmap.fromImage(image[0]))
        pred_label = QLabel(self)
        pred_label.move(x_offset, 420)
        pred_label.resize(150, 150)
        pred_label.setText("Prediction: {}".format(image[1]))
        conf_label = QLabel(self)
        conf_label.move(x_offset, 430)
        conf_label.resize(150, 150)
        conf_label.setText("Confidence: {}".format(image[2]))
        sec_label = QLabel(self)
        sec_label.move(x_offset, 440)
        sec_label.resize(150, 150)
        sec_label.setText("Second: {}".format(str(image[3])))
        img_label.show()
        pred_label.show()
        conf_label.show()
        sec_label.show()

    def _initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(900, 600)
        self._create_main_image()
        self._create_thread()

    def _create_main_image(self):
        self.img_label = QLabel(self)
        self.img_label.move(300, -150)
        self.img_label.resize(600, 600)
        self.conf_label = QLabel(self)
        self.conf_label.setFont(QFont("Arial", 10))
        self.conf_label.move(0, 200)
        self.conf_label.resize(600, 140)
        self.delay_label = QLabel(self)
        self.delay_label.setFont(QFont("Arial", 10))
        self.delay_label.move(0, 220)
        self.delay_label.resize(600, 140)
        self.pred_label = QLabel(self)
        self.pred_label.setFont(QFont("Arial", 10))
        self.pred_label.move(0, 240)
        self.pred_label.resize(600, 140)

        
    def _create_thread(self):
        self.th = Thread(self)
        self.th.change_pixmap.connect(self.set_main_image)
        self.th.change_conf_label.connect(self.set_conf_label)
        self.th.change_delay_label.connect(self.set_delay_label)
        self.th.change_pred_label.connect(self.set_pred_label)
        self.th.add_image.connect(self.add_image)
        self.th.show_result.connect(self.show_result)
        self.th.server_name = self.server_name
        self.th.server_port = self.server_port
        self.th.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.th.client_socket.connect((self.server_name, self.server_port))
        self.th.start()

    def closeEvent(self, event):
        if self.th:
            self.th.finish = False
            self.th.terminate()
            self.destroy()
            self.parent().show()

    def show_result(self):
        final_pred = self._get_final_pred()
        self.img_label.destroy()
        self.img_label.clear()
        self.conf_label.destroy()
        self.delay_label.destroy()
        self.pred_label.destroy()
        self.result_label = QLabel(self)
        self.result_label.setText(f"Result:{final_pred}")
        self.result_label.setFont(QFont("Arial", 30))
        self.result_label.move(300, -150)
        self.result_label.resize(600, 600)
        self.result_label.show()
        
    def _get_final_pred(self):
        with_mask_res = sum([img for img in self.images_list if img[1] == "with_mask"])
        without_mask_res = len(self.images_list) - with_mask_res
        return "with_mask" if with_mask_res > without_mask_res else "without_mask"
            

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./ui/main_window.ui", self)
        self._initUI()
        self.show()

    def _initUI(self):
        self.resize(900, 600)
        start_button = self._make_start_button()

    def _make_start_button(self):
        button = QPushButton(self)
        button.setText("Start")
        button.move(400, 400)
        button.clicked.connect(self._on_start_button_clicked)
        return button

    def _on_start_button_clicked(self):
        self.detect_window = DetectWindow(self, "pc", 8006)
        self.detect_window.move(500, 100)
        self.hide()
        self.detect_window.show()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    # ex = App("ubuntu", 8007)
    # ex = App("DESKTOP-HT34P2E", 8006)
    sys.exit(app.exec_())
