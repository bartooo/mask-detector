import typing
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import QImage
import struct
import pickle
import cv2
from PyQt5.QtCore import Qt
import threading
import datetime


class Thread(QThread):
    def __init__(self, parent: typing.Optional[QObject]) -> None:
        super().__init__(parent=parent)
        self._finish = False
        self._run_seconds = 1
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
        try:
            while not self.finish and self.run_seconds < 6:
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
                self.frame = convertToQtFormat.scaled(150, 150, Qt.KeepAspectRatio)
                self.confidence = f"{data_recv.percentage:.3f}"
                self.prediction = f"{data_recv.decision}"
                self.change_pixmap.emit(
                    convertToQtFormat.scaled(350, 350, Qt.KeepAspectRatio)
                )
                self.change_conf_label.emit(f"Confidence: {self.confidence}%")
                if type(data_recv.time_sended) is datetime.timedelta:
                    self.change_delay_label.emit(
                        # f"Delay: {(datetime.datetime.now() - data_recv.time_sended).total_seconds() * 1000:.3f} ms"
                        f"Delay: {data_recv.time_sended.total_seconds()*1000:.3f} ms"
                    )
                self.change_pred_label.emit(f"Prediction: {self.prediction}")
                if self.run_seconds == 1:
                    self._send_frame()

                elif self.run_seconds == 6:
                    self.timer.cancel()

            self.client_socket.close()
            self.show_result.emit()
        except (struct.error) as e:
            self.client_socket.close()
        

    def _send_frame(self):
        self.add_image.emit(
            self.frame, self.confidence, self.prediction, self.run_seconds
        )
        self.run_seconds += 1
        self.timer = threading.Timer(1.0, self._send_frame)
        self.timer.start()
