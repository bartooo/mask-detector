from PyQt5 import QtWidgets
from Thread import Thread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont, QImage, QPixmap
from DetectorExceptions.ConnectionExceptions import validate_port
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
import socket


class DetectWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        validate_port(parent.server_port)
        self.server_name = parent.server_name
        self.server_port = parent.server_port
        self.images_list = []
        self.images_labels = []
        self.images_vboxes = []
        self._initUI()
        self._create_thread()
        self.result_label = None
        self.during_detection = True

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
        x_offset = 180 + ((len(self.images_list) - 1) * 200)
        img_label.resize(
            QPixmap.fromImage(image[0]).width() + 5,
            QPixmap.fromImage(image[0]).height() + 7,
        )
        img_label.setPixmap(QPixmap.fromImage(image[0]))
        img_label.move(x_offset, 420)
        img_label.setStyleSheet("background-color:#dbac3b")
        pred_label = QLabel(self)
        pred_label.setText("Prediction: {}".format(image[2]))
        pred_label.setFont(QFont("Calibri Light", 10))
        pred_label.move(x_offset, 520)
        pred_label.resize(200, 10)
        conf_label = QLabel(self)
        conf_label.setFont(QFont("Calibri Light", 10))
        conf_label.move(x_offset, 530)
        conf_label.resize(150, 10)
        conf_label.setText("Confidence: {}%".format(image[1]))
        sec_label = QLabel(self)
        sec_label.setFont(QFont("Calibri Light", 10))
        sec_label.move(x_offset, 540)
        sec_label.resize(150, 10)
        sec_label.setText("Second: {}".format(str(image[3])))
        self._add_to_images_labels_list(img_label, pred_label, conf_label, sec_label)
        pred_label.setStyleSheet("color: white")
        conf_label.setStyleSheet("color: white")
        sec_label.setStyleSheet("color: white")
        img_label.show()
        pred_label.show()
        conf_label.show()
        sec_label.show()

    def _initUI(self):
        self.resize(1280, 720)
        self._create_main_image()
        self.detect_button = self._create_detect_again_button()
        self.back_button = self._create_back_button()
        self.setStyleSheet("background-color : #2f2e2e")

    def _create_main_image(self):
        self.img_label = QLabel(self)
        self.img_label.resize(355, 355)
        self.img_label.move(self.width() / 2 - 200, 5)
        self.conf_label = QLabel(self)
        self.conf_label.setFont(QFont("Calibri Light", 10))
        self.conf_label.setStyleSheet("color: white")
        self.conf_label.move(0, 200)
        self.conf_label.resize(200, 20)
        self.delay_label = QLabel(self)
        self.delay_label.setFont(QFont("Calibri Light", 10))
        self.delay_label.setStyleSheet("color: white")
        self.delay_label.move(0, 220)
        self.delay_label.resize(300, 20)
        self.pred_label = QLabel(self)
        self.pred_label.setFont(QFont("Calibri Light", 10))
        self.pred_label.setStyleSheet("color: white")
        self.pred_label.move(0, 240)
        self.pred_label.resize(300, 20)

    def _create_thread(self):
        self.th = Thread(self)
        self.th.change_pixmap.connect(self.set_main_image)
        self.th.change_conf_label.connect(self.set_conf_label)
        self.th.change_delay_label.connect(self.set_delay_label)
        self.th.change_pred_label.connect(self.set_pred_label)
        self.th.add_image.connect(self.add_image)
        self.th.show_result.connect(self.show_result)
        self._update_server_info()
        self.th.server_name = self.server_name
        self.th.server_port = self.server_port
        self.th.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.th.client_socket.connect((self.server_name, self.server_port))
        self.th.start()

    def _update_server_info(self):
        self.server_name = self.parent().server_name
        self.server_port = self.parent().server_port

    def _create_detect_again_button(self):
        button = QPushButton(self)
        button.setText("Detect again")
        button.setStyleSheet("QPushButton {background-color:#dbac3b; color:white}")
        button.move(5, 20)
        button.clicked.connect(self._on_detect_again_button_clicked)
        return button

    def _on_detect_again_button_clicked(self):
        # let user detect again only if previous detection is done
        if not self.during_detection:
            self.during_detection = True
            self.images_list.clear()
            self._clear_images_labels()
            self._create_thread()

    def _create_back_button(self):
        button = QPushButton(self)
        button.setText("Back")
        button.setStyleSheet("QPushButton {background-color:#dbac3b; color:white}")
        button.move(1200, 20)
        button.clicked.connect(self._on_back_button_clicked)
        return button

    def _on_back_button_clicked(self):
        if not self.during_detection:
            self._destroy_thread()
            self.parent().show()
            self.destroy()

    def _clear_images_labels(self):
        for label in self.images_labels:
            label.clear()
            label.hide()

        if self.result_label:
            self.result_label.clear()
            self.result_label.hide()

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
        self.during_detection = False
        self._destroy_thread()
        self._clear_stats_labels()
        final_pred = self._get_final_pred()
        self.img_label.destroy()
        self.img_label.clear()
        self.conf_label.destroy()
        self.delay_label.destroy()
        self.pred_label.destroy()
        self.result_label = QLabel(self)
        self.result_label.setStyleSheet("color: white")
        self.result_label.setText(f"Result:{final_pred}")
        self.result_label.setFont(QFont("Calibri Light", 30))
        self.result_label.resize(400, 50)
        self.result_label.move(int(self.width() // 2 - 200), 150)
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
