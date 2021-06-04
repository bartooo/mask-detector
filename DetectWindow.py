from Thread import Thread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont, QImage, QPixmap
from DetectorExceptions.ConnectionExceptions import validate_port
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
import socket

class DetectWindow(QDialog):
    def __init__(self, parent, serv_name: str, serv_port: int):
        super().__init__(parent=parent)
        validate_port(serv_port)
        self.server_name = serv_name
        self.server_port = serv_port
        self.images_list = []
        self.images_labels = []
        self.images_vboxes = []
        self._initUI()
        self._create_thread()
        self.result_label = None

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
        self._display_image(self.images_list[len(self.images_list) - 1])

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
        self._add_to_images_labels_list(img_label, pred_label, conf_label, sec_label)
        img_label.show()
        pred_label.show()
        conf_label.show()
        sec_label.show()

    def _initUI(self):
        self.resize(1280, 720)
        self._create_main_image()
        self.detect_button = self._create_detect_again_button()
        

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

    def _create_detect_again_button(self):
        button = QPushButton(self)
        button.setText("Detect again")
        button.clicked.connect(self._on_create_detect_again_button_clicked)
        return button

    def _on_create_detect_again_button_clicked(self):
        # let user detect again only if previous detection is done
        if self.result_label:
            self.images_list.clear()
            self._clear_images_labels()
            self._create_thread()

    def _clear_images_labels(self):
        for label in self.images_labels:
            label.clear()
            
        if self.result_label:
            self.result_label.clear()
        
    def _clear_stats_labels(self):
        self.img_label.clear()
        self.pred_label.clear()
        self.conf_label.clear()
        self.delay_label.clear()
        
    def _add_to_images_labels_list(self, *args):
        for arg in args:
            self.images_labels.append(arg)

    def closeEvent(self, event):
        self._destroy_thread()
        self.destroy()
        self.parent().show()

    def show_result(self):
        self._destroy_thread()
        self._clear_stats_labels()
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

    def _destroy_thread(self):
        if self.th:
            self.th.finish = False
            self.th.terminate()
            self.th = None

    def _get_final_pred(self):
        results = {"with_mask": 0, "without_mask": 0, "no face detected": 0}
        for img in self.images_list:
            results[img[2]] += 1

        return max(results, key=results.get)