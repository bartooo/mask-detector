from PyQt5 import QtCore, QtWidgets
from Thread import Thread
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QCursor, QFont, QImage, QPixmap
from DetectorExceptions.ConnectionExceptions import validate_port
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
import socket
from DetectWindowUI import Ui_DetectDialog


class DetectWindow(QDialog, Ui_DetectDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        self._setup_dict()
        self._connect_buttons()
        self._setup_cursors()
        validate_port(parent.server_port)
        self.server_name = parent.server_name
        self.server_port = parent.server_port
        self.images_list = []
        self._hide_image_labels()
        self.show_stats_labels()
        self._create_thread()
        

    @pyqtSlot(QImage)
    def set_main_image(self, image):
        self.main_image_label.setPixmap(QPixmap.fromImage(image))

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
        self._display_image_of_second(second)

    def _setup_dict(self):
        self.images_labels_dict = {
            1: {
                "image": self.image_label_1,
                "pred": self.pred_label_1,
                "conf": self.conf_label_1,
                "sec": self.sec_label_1,
            },
            2: {
                "image": self.image_label_2,
                "pred": self.pred_label_2,
                "conf": self.conf_label_2,
                "sec": self.sec_label_2,
            },
            3: {
                "image": self.image_label_3,
                "pred": self.pred_label_3,
                "conf": self.conf_label_3,
                "sec": self.sec_label_3,
            },
            4: {
                "image": self.image_label_4,
                "pred": self.pred_label_4,
                "conf": self.conf_label_4,
                "sec": self.sec_label_4,
            },
            5: {
                "image": self.image_label_5,
                "pred": self.pred_label_5,
                "conf": self.conf_label_5,
                "sec": self.sec_label_5,
            },
        }

    def _setup_cursors(self):
        self.back_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.detect_again_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def _hide_image_labels(self):
        for sec in range(1, 6):
            for i in {"image", "pred", "conf", "sec"}:
                self.images_labels_dict[sec][i].setProperty("is_hidden", "true")
                self.images_labels_dict[sec][i].style().unpolish(self.images_labels_dict[sec][i])
                self.images_labels_dict[sec][i].style().polish(self.images_labels_dict[sec][i])
                self.images_labels_dict[sec][i].update()

    def _connect_buttons(self):
        self.back_button.clicked.connect(self._on_back_button_clicked)
        self.detect_again_button.clicked.connect(self._on_detect_again_button_clicked)

    def _display_image_of_second(self, second):
        for label_type in {"image", "pred", "conf", "sec"}:
            self.images_labels_dict[second][label_type].setProperty("is_hidden", "false")
            self.images_labels_dict[second][label_type].style().unpolish(self.images_labels_dict[second][label_type])
            self.images_labels_dict[second][label_type].style().polish(self.images_labels_dict[second][label_type])
            self.images_labels_dict[second][label_type].update()
        
        self.images_labels_dict[second]["image"].setPixmap(
            QPixmap.fromImage(self.images_list[second - 1][0])
        )
        self.images_labels_dict[second]["conf"].setText(
            "Confidence: {}%".format(self.images_list[second - 1][1])
        )
        self.images_labels_dict[second]["pred"].setText(
            "Prediction: {}".format(self.images_list[second - 1][2])
        )
        self.images_labels_dict[second]["sec"].setText(
            "Second: {}".format(str(self.images_list[second - 1][3]))
        )

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

    def _on_detect_again_button_clicked(self):
        if self._is_thread_finished():
            self.images_list.clear()
            self._clear_images_labels()
            self.show_stats_labels()
            self._hide_image_labels()
            self._create_thread()

    def _on_back_button_clicked(self):
        if self._is_thread_finished():
            self._destroy_thread()
            self.parent().show()
            self.destroy()

    def _is_thread_finished(self):
        return self.th is None or self.th.isFinished()

    def _clear_images_labels(self):
        for sec in range(1, 6):
            for i in {"image", "pred", "conf", "sec"}:
                self.images_labels_dict[sec][i].clear()

    def _clear_stats_labels(self):
        self.main_image_label.clear()
        self.main_image_label.setProperty("is_hidden", "true")
        self.main_image_label.style().unpolish(self.main_image_label)
        self.main_image_label.style().polish(self.main_image_label)
        self.main_image_label.update()
        self.pred_label.clear()
        self.pred_label.setProperty("is_hidden", "true")
        self.pred_label.style().unpolish(self.pred_label)
        self.pred_label.style().polish(self.pred_label)
        self.pred_label.update()
        self.conf_label.clear()
        self.conf_label.setProperty("is_hidden", "true")
        self.conf_label.style().unpolish(self.conf_label)
        self.conf_label.style().polish(self.conf_label)
        self.conf_label.update()
        self.delay_label.clear()
        self.delay_label.setProperty("is_hidden", "true")
        self.delay_label.style().unpolish(self.delay_label)
        self.delay_label.style().polish(self.delay_label)
        self.delay_label.update()

    def closeEvent(self, event):
        self._destroy_thread()
        self.destroy()
        self.parent().show()

    def show_result(self):
        self._destroy_thread()
        self._clear_stats_labels()
        self.conf_label.destroy()
        self.delay_label.destroy()
        self.pred_label.destroy()
        self.main_image_label.setText(f"Result : {self._get_final_pred()}")
        self._destroy_thread()

    def _destroy_thread(self):
        if self.th:
            self.th.finish = True
            self.th.quit()
            self.th = None

    def _get_final_pred(self):
        results = {"with_mask": 0, "without_mask": 0, "no face detected": 0}
        for img in self.images_list:
            results[img[2]] += 1

        return max(results, key=results.get)
    
    def show_stats_labels(self):
        self.main_image_label.setProperty("is_hidden", "false")
        self.main_image_label.style().unpolish(self.main_image_label)
        self.main_image_label.style().polish(self.main_image_label)
        self.main_image_label.update()
        self.pred_label.setProperty("is_hidden", "false")
        self.pred_label.style().unpolish(self.pred_label)
        self.pred_label.style().polish(self.pred_label)
        self.pred_label.update()
        self.conf_label.setProperty("is_hidden", "false")
        self.conf_label.style().unpolish(self.conf_label)
        self.conf_label.style().polish(self.conf_label)
        self.conf_label.update()
        self.delay_label.setProperty("is_hidden", "false")
        self.delay_label.style().unpolish(self.delay_label)
        self.delay_label.style().polish(self.delay_label)
        self.delay_label.update()