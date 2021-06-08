from PyQt5 import QtCore, QtGui, QtWidgets
from ClientDetector.ClientThread import ClientThread
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtGui import QCursor, QFont, QImage, QPixmap
from DetectorExceptions.ConnectionExceptions import validate_port
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
import socket
from ClientDetector.pyui.DetectWindowUI import Ui_DetectDialog
from ClientDetector.ResultWindow import ResultWindow


class DetectWindow(QDialog, Ui_DetectDialog):
    """Class represents Detection Window for GUI."""

    def __init__(self, parent: QObject, logging_enabled: bool) -> None:
        """DetectWindow constructor.

        Args:
            parent (QObject): parent of dialog
            logging_enabled (bool): tells if logging is enabled
        """
        super().__init__(parent=parent)
        self.setupUi(self)
        self._setup_window()
        self._setup_dict()
        self._connect_buttons()
        self._setup_cursors()
        validate_port(parent.server_port)
        self.server_name = parent.server_name
        self.server_port = parent.server_port
        self.images_list = []
        self.logging_enabled = logging_enabled
        self._hide_image_labels()
        self.show_stats_labels()
        self._create_thread()

    @pyqtSlot(QImage)
    def set_main_image(self, image: QImage) -> None:
        """Setting main_image label.

        Args:
            image (QImage): new image
        """
        self.main_image_label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str)
    def set_conf_label(self, conf: str) -> None:
        """Setting confidence label

        Args:
            conf (str): new confidence
        """
        self.conf_label.setText(f"Confidence: {conf}%")

    @pyqtSlot(str)
    def set_delay_label(self, delay: str) -> None:
        """Setting delay label

        Args:
            delay (str): new delay
        """
        self.delay_label.setText(f"Delay: {delay} ms")

    @pyqtSlot(str)
    def set_pred_label(self, pred: str) -> None:
        """Setting prediction label.

        Args:
            pred (str): new prediction
        """
        self.pred_label.setText(f"Prediction: {pred}")

    @pyqtSlot(QImage, str, str, int)
    def add_image(
        self, image: QImage, prediction: str, confidence: str, second: int
    ) -> None:
        """Function adds image with correct labels and its properties on given second.

        Args:
            image (QImage): image to display
            prediction (str): prediction
            confidence (str): confidence
            second (int): second of detection
        """
        self.images_list.append((image, prediction, confidence, second))
        self._display_image_of_second(second)

    def _setup_window(self) -> None:
        """Function setup window's title and icon."""
        self.setWindowIcon(QtGui.QIcon("ClientDetector/resources/logo.png"))
        self.setWindowTitle("REAL-TIME FACE MASK DETECTOR")

    def _setup_dict(self) -> None:
        """Function creates dict of labels."""
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

    def _setup_cursors(self) -> None:
        """Function setups cursors on buttons."""
        self.back_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.detect_again_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def _hide_image_labels(self) -> None:
        """Function hides labels' images."""
        for sec in range(1, 6):
            for i in {"image", "pred", "conf", "sec"}:
                self._change_label_property(
                    self.images_labels_dict[sec][i], "is_hidden", "true"
                )

    def _connect_buttons(self) -> None:
        """Function connects buttons to its actions."""
        self.back_button.clicked.connect(self._on_back_button_clicked)
        self.detect_again_button.clicked.connect(self._on_detect_again_button_clicked)

    def _display_image_of_second(self, second: int) -> None:
        """Function displays labels for given second.

        Args:
            second (int): second of detection
        """
        for label_type in {"image", "pred", "conf", "sec"}:
            self._change_label_property(
                self.images_labels_dict[second][label_type], "is_hidden", "false"
            )

        self.images_labels_dict[second]["image"].setPixmap(
            QPixmap.fromImage(self.images_list[second - 1][0])
        )
        self.images_labels_dict[second]["conf"].setText(
            "Confidence: {}%".format(self.images_list[second - 1][1])
        )
        self.images_labels_dict[second]["pred"].setText(
            "Prediction: {}".format(self.images_list[second - 1][2].replace("_", " "))
        )
        self.images_labels_dict[second]["sec"].setText(
            "Second: {}".format(str(self.images_list[second - 1][3]))
        )

    def _create_thread(self) -> None:
        """Function creates thread for connection."""
        self.th = ClientThread(self)
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

    def _update_server_info(self) -> None:
        """Function updates server_name and server_port params."""
        self.server_name = self.parent().server_name
        self.server_port = self.parent().server_port

    def _on_detect_again_button_clicked(self) -> None:
        """Function starts detection again when clicking on again button."""
        if self._is_thread_finished():
            self.images_list.clear()
            self._clear_images_labels()
            self.show_stats_labels()
            self._hide_image_labels()
            self._create_thread()

    def _on_back_button_clicked(self) -> None:
        """Function destroys window when clicking on back button."""
        if self._is_thread_finished():
            self._destroy_thread()
            self.parent().show()
            self.destroy()

    def _is_thread_finished(self) -> bool:
        """Function checks if thread is finished

        Returns:
            [bool]: returns true if thread is not running
        """
        return self.th is None or self.th.isFinished()

    def _clear_images_labels(self) -> None:
        """Function clear all labels."""
        for sec in range(1, 6):
            for i in {"image", "pred", "conf", "sec"}:
                self.images_labels_dict[sec][i].clear()

    def _clear_stats_labels(self) -> None:
        """Function hides all labels."""
        self.main_image_label.clear()
        self._change_label_property(self.main_image_label, "is_hidden", "true")
        self.pred_label.clear()
        self._change_label_property(self.pred_label, "is_hidden", "true")
        self.conf_label.clear()
        self._change_label_property(self.conf_label, "is_hidden", "true")
        self.delay_label.clear()
        self._change_label_property(self.delay_label, "is_hidden", "true")

    def closeEvent(self, event: QEvent) -> None:
        """Handler of DetectWindow closure.

        Args:
            event (QEvent): event to be overrided
        """
        self._destroy_thread()
        self.destroy()
        self.parent().show()

    def show_result(self) -> None:
        """Function shows result window."""
        self._destroy_thread()
        resultDialog = ResultWindow(self._get_final_pred(), parent=self)
        resultDialog.show()

    def _destroy_thread(self) -> None:
        """Function destroys thread connecting with server."""
        if self.th:
            self.th.finish = True
            self.th.quit()
            self.th = None

    def _get_final_pred(self) -> str:
        """Function returns final predictions for a period.

        Returns:
            str: final prediction
        """
        results = {"with_mask": 0, "without_mask": 0, "NO FACE": 0, "MULTIPLE FACES": 0}
        for img in self.images_list:
            results[img[2]] += 1

        return max(results, key=results.get).replace("_", " ")

    def _change_label_property(
        self, label: QObject, property_name: str, property_value: str
    ) -> None:
        """Function changes given label property.

        Args:
            label (QObject): label to change property for
            property_name (str): name of property to change
            property_value (str): new value of property
        """
        label.setProperty(property_name, property_value)
        label.style().unpolish(label)
        label.style().polish(label)
        label.update()

    def show_stats_labels(self) -> None:
        """Function shows statistics labels."""
        self.main_image_label.clear()
        self._change_label_property(self.main_image_label, "is_hidden", "false")
        self._change_label_property(self.pred_label, "is_hidden", "false")
        self._change_label_property(self.conf_label, "is_hidden", "false")
        self._change_label_property(self.delay_label, "is_hidden", "false")
