from PyQt5 import QtWidgets
from Thread import Thread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont, QImage, QPixmap
from DetectorExceptions.ConnectionExceptions import validate_port
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
import socket
from DetectWindowUI import Ui_DetectDialog


class DetectWindow(QDialog, Ui_DetectDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
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
        self._connect_buttons()
        validate_port(parent.server_port)
        self.server_name = parent.server_name
        self.server_port = parent.server_port
        self.images_list = []
        self._hide_image_labels()
        self._create_thread()
        self.result_label = None
        self.during_detection = True
        

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

    def _hide_image_labels(self):
        for sec in range(1, 6):
            for i in {"image", "pred", "conf", "sec"}:
                self.images_labels_dict[sec][i].setStyleSheet(
                    "QLabel {\n" "border: 0px solid gold;\n" "}"
                )

    def _connect_buttons(self):
        self.back_button.clicked.connect(self._on_back_button_clicked)
        self.detect_again_button.clicked.connect(self._on_detect_again_button_clicked)

    def _display_image_of_second(self, second):
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
        self.set_style_image_labels(second)

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
        # let user detect again only if previous detection is done
        if self.th is None or self.th.isFinished():
            self.during_detection = True
            self.images_list.clear()
            self._clear_images_labels()
            self.show_stats_labels()
            self._hide_image_labels()
            self._create_thread()

    def _on_back_button_clicked(self):
        if self.th is None or not self.th.isRunning():
            self._destroy_thread()
            self.parent().show()
            self.destroy()

    def _clear_images_labels(self):
        for sec in range(1, 6):
            for i in {"image", "pred", "conf", "sec"}:
                self.images_labels_dict[sec][i].clear()

        if self.result_label:
            self.result_label.clear()
            self.result_label.hide()

    def _clear_stats_labels(self):
        self.main_image_label.clear()
        self.main_image_label.setStyleSheet("QLabel{\n" "border: 0px solid gold;\n" "}")
        self.pred_label.clear()
        self.pred_label.setStyleSheet("QLabel {\n" "border: 0px solid gold;\n" "}")
        self.conf_label.clear()
        self.conf_label.setStyleSheet("QLabel {\n" "border: 0px solid gold;\n" "}")
        self.delay_label.clear()
        self.delay_label.setStyleSheet("QLabel {\n" "border: 0px solid gold;\n" "}")

    def closeEvent(self, event):
        self._destroy_thread()
        self.destroy()
        self.parent().show()

    def show_result(self):
        self._destroy_thread()
        self._clear_stats_labels()
        final_pred = self._get_final_pred()
        self.main_image_label.destroy()
        self.main_image_label.clear()
        self.conf_label.destroy()
        self.delay_label.destroy()
        self.pred_label.destroy()
        self.result_label = QLabel(self)
        self.result_label.setStyleSheet(
            "QLabel {\n"
            "font-family: sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 22px;\n"
            "font-weight: bold;\n"
            "}"
        )
        self.result_label.setText(f"Result : {final_pred}")
        self.result_label.resize(400, 50)
        self.result_label.move(900, 150)
        self.result_label.show()
        self._destroy_thread()
        self.during_detection = False

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
        self.main_image_label.setStyleSheet(
            "QLabel{\n" "border: 3px solid gold;\n" "border-radius: 10px;\n" "}"
        )
        self.pred_label.setStyleSheet(
            "QLabel {\n"
            "border: 2px solid gold;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 14px;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.conf_label.setStyleSheet(
            "QLabel {\n"
            "border: 2px solid gold;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 14px;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.delay_label.setStyleSheet(
            "QLabel {\n"
            "border: 2px solid gold;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 14px;\n"
            "border-radius: 10px;\n"
            "}"
        )

    def set_style_image_labels(self, second):
        self.images_labels_dict[second]["image"].setStyleSheet(
            "QLabel {\n"
            "border: 2px solid gold;\n"
            "font-family:sans-serif;\n"
            "color: white;\n"
            "font-size: 14px;\n"
            "text-align: center;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.images_labels_dict[second]["conf"].setStyleSheet(
            "QLabel {\n"
            "border: 2px solid gold;\n"
            "font-family:sans-serif;\n"
            "color: white;\n"
            "font-size: 14px;\n"
            "text-align: center;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.images_labels_dict[second]["pred"].setStyleSheet(
            "QLabel {\n"
            "border: 2px solid gold;\n"
            "font-family:sans-serif;\n"
            "color: white;\n"
            "font-size: 14px;\n"
            "text-align: center;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.images_labels_dict[second]["sec"].setStyleSheet(
            "QLabel {\n"
            "border: 2px solid gold;\n"
            "font-family:sans-serif;\n"
            "color: white;\n"
            "font-size: 14px;\n"
            "text-align: center;\n"
            "border-radius: 10px;\n"
            "}"
        )
