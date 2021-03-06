# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\detect_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DetectDialog(object):
    def setupUi(self, DetectDialog):
        DetectDialog.setObjectName("DetectDialog")
        DetectDialog.resize(1080, 620)
        DetectDialog.setMinimumSize(QtCore.QSize(1080, 620))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        DetectDialog.setFont(font)
        DetectDialog.setStyleSheet(
            "QDialog{\n"
            "color: #cfab2d;\n"
            "background-color: #2a292e;\n"
            "border: 3px solid #cfab2d;\n"
            "border-radius: 10px;}\n"
            "   "
        )
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(DetectDialog)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.main_vlayout = QtWidgets.QVBoxLayout()
        self.main_vlayout.setObjectName("main_vlayout")
        self.title_label = QtWidgets.QLabel(DetectDialog)
        self.title_label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        # font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(
            "QLabel{\n"
            "    color: #cfab2d;\n"
            "    text-align: center;\n"
            "    margin: 0 auto;\n"
            "    font-weight: bold;\n"
            "    font-size: 24px;\n"
            "    font-family: sans-serif;\n"
            "    text-transform: uppercase;\n"
            "    letter-spacing: 0.1em;\n"
            "}"
        )
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.main_vlayout.addWidget(self.title_label)
        self.buttons_photo_hlayout = QtWidgets.QHBoxLayout()
        self.buttons_photo_hlayout.setObjectName("buttons_photo_hlayout")
        self.label_buttons_vlayout = QtWidgets.QVBoxLayout()
        self.label_buttons_vlayout.setObjectName("label_buttons_vlayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.label_buttons_vlayout.addItem(spacerItem)
        self.labels_vlayout = QtWidgets.QVBoxLayout()
        self.labels_vlayout.setContentsMargins(0, -1, -1, -1)
        self.labels_vlayout.setObjectName("labels_vlayout")
        self.delay_label = QtWidgets.QLabel(DetectDialog)
        self.delay_label.setMaximumSize(QtCore.QSize(300, 40))
        self.delay_label.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 2px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "text-align: center;\n"
            "color: #cfab2d;\n"
            "font-size: 16px;\n"
            "font-weight: bold;\n"
            "border-radius: 10px;\n"
            "letter-spacing: 0.1em;\n"
            "text-transform: uppercase;\n"
            "min-width: 300px;\n"
            "min-height: 40px;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 0px solid black;\n"
            "}"
        )
        self.delay_label.setText("")
        self.delay_label.setAlignment(QtCore.Qt.AlignCenter)
        self.delay_label.setObjectName("delay_label")
        self.labels_vlayout.addWidget(self.delay_label, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.labels_vlayout.addItem(spacerItem1)
        self.conf_label = QtWidgets.QLabel(DetectDialog)
        self.conf_label.setMaximumSize(QtCore.QSize(300, 40))
        self.conf_label.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 2px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "text-align: center;\n"
            "color: #cfab2d;\n"
            "font-size: 16px;\n"
            "font-weight: bold;\n"
            "border-radius: 10px;\n"
            "letter-spacing: 0.1em;\n"
            "text-transform: uppercase;\n"
            "min-width: 300px;\n"
            "min-height: 40px;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 0px soild black;\n"
            "}"
        )
        self.conf_label.setText("")
        self.conf_label.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_label.setObjectName("conf_label")
        self.labels_vlayout.addWidget(self.conf_label, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.labels_vlayout.addItem(spacerItem2)
        self.pred_label = QtWidgets.QLabel(DetectDialog)
        self.pred_label.setMinimumSize(QtCore.QSize(0, 0))
        self.pred_label.setMaximumSize(QtCore.QSize(300, 40))
        self.pred_label.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 2px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "text-align: center;\n"
            "color: #cfab2d;\n"
            "font-size: 14px;\n"
            "font-weight: bold;\n"
            "border-radius: 10px;\n"
            "letter-spacing: 0.1em;\n"
            "text-transform: uppercase;\n"
            "min-width: 300px;\n"
            "min-height: 40px;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 0px solid black;\n"
            "}"
        )
        self.pred_label.setText("")
        self.pred_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_label.setObjectName("pred_label")
        self.labels_vlayout.addWidget(self.pred_label, 0, QtCore.Qt.AlignHCenter)
        self.label_buttons_vlayout.addLayout(self.labels_vlayout)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.label_buttons_vlayout.addItem(spacerItem3)
        self.buttons_hlayout = QtWidgets.QHBoxLayout()
        self.buttons_hlayout.setContentsMargins(0, -1, 0, -1)
        self.buttons_hlayout.setObjectName("buttons_hlayout")
        self.detect_again_button = QtWidgets.QPushButton(DetectDialog)
        self.detect_again_button.setMinimumSize(QtCore.QSize(0, 0))
        self.detect_again_button.setMaximumSize(QtCore.QSize(177, 16777215))
        self.detect_again_button.setStyleSheet(
            "/*QPushButton {\n"
            "border: 2px solid gold;\n"
            "font: sans-serif;\n"
            "color: #cfab2d;\n"
            "background-color: #2a292e;\n"
            "text-align: center;\n"
            "font-size: 12px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border: 2px solid gold;\n"
            'font: 13 px "sans-serif";\n'
            "color:#2a292e;\n"
            "background-color: #cfab2d;\n"
            "}\n"
            "*/\n"
            "QPushButton{\n"
            "    color: #cfab2d;\n"
            "    background-color: #2a292e;\n"
            "    text-align: center;\n"
            "    max-width: 33em;\n"
            "    width: 9em;\n"
            "    font-size: 16px;\n"
            "    height: 2em;\n"
            "    font-weight: bold;\n"
            "    font-family: sans-serif;\n"
            "    text-transform: uppercase;\n"
            "    letter-spacing: 0.1em;\n"
            "    border: 3px solid #cfab2d;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    color:#2a292e;\n"
            "    background-color: #cfab2d;\n"
            "}"
        )
        self.detect_again_button.setObjectName("detect_again_button")
        self.buttons_hlayout.addWidget(self.detect_again_button)
        self.back_button = QtWidgets.QPushButton(DetectDialog)
        self.back_button.setMinimumSize(QtCore.QSize(0, 0))
        self.back_button.setMaximumSize(QtCore.QSize(177, 16777215))
        self.back_button.setStyleSheet(
            "/*QPushButton {\n"
            "border: 2px solid gold;\n"
            "font: sans-serif;\n"
            "color: #cfab2d;\n"
            "background-color: #2a292e;\n"
            "text-align: center;\n"
            "font-size: 12px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border: 2px solid gold;\n"
            'font: 13 px "sans-serif";\n'
            "color:#2a292e;\n"
            "background-color: #cfab2d;\n"
            "}\n"
            "*/\n"
            "QPushButton{\n"
            "    color: #cfab2d;\n"
            "    background-color: #2a292e;\n"
            "    text-align: center;\n"
            "    max-width: 33em;\n"
            "    width: 9em;\n"
            "    font-size: 16px;\n"
            "    height: 2em;\n"
            "    font-weight: bold;\n"
            "    font-family: sans-serif;\n"
            "    text-transform: uppercase;\n"
            "    letter-spacing: 0.1em;\n"
            "    border: 3px solid #cfab2d;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    color:#2a292e;\n"
            "    background-color: #cfab2d;\n"
            "}"
        )
        self.back_button.setObjectName("back_button")
        self.buttons_hlayout.addWidget(self.back_button)
        self.label_buttons_vlayout.addLayout(self.buttons_hlayout)
        self.buttons_photo_hlayout.addLayout(self.label_buttons_vlayout)
        self.main_image_label = QtWidgets.QLabel(DetectDialog)
        self.main_image_label.setMinimumSize(QtCore.QSize(300, 300))
        self.main_image_label.setMaximumSize(QtCore.QSize(300, 300))
        self.main_image_label.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 3px solid #cfab2d;\n"
            "border-radius: 10px;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "font-family:sans-serif;\n"
            "text-align: center;\n"
            "color: #cfab2d;\n"
            "font-size: 14px;\n"
            "font-weight: bold;\n"
            "letter-spacing: 0.1em;\n"
            "text-transform: uppercase;\n"
            "}"
        )
        self.main_image_label.setText("")
        self.main_image_label.setObjectName("main_image_label")
        self.buttons_photo_hlayout.addWidget(self.main_image_label)
        self.main_vlayout.addLayout(self.buttons_photo_hlayout)
        self.line = QtWidgets.QFrame(DetectDialog)
        self.line.setStyleSheet("\n" "background-color: #cfab2d;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_vlayout.addWidget(self.line)
        self.history_hlayout = QtWidgets.QHBoxLayout()
        self.history_hlayout.setObjectName("history_hlayout")
        self.history_1_vlayout = QtWidgets.QVBoxLayout()
        self.history_1_vlayout.setObjectName("history_1_vlayout")
        self.image_label_1 = QtWidgets.QLabel(DetectDialog)
        self.image_label_1.setMinimumSize(QtCore.QSize(150, 150))
        self.image_label_1.setMaximumSize(QtCore.QSize(150, 150))
        self.image_label_1.setStyleSheet(
            "\n"
            'QLabel[is_hidden="false"]{\n'
            "border: 3px solid #cfab2d;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 3px solid #2a292e;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.image_label_1.setText("")
        self.image_label_1.setObjectName("image_label_1")
        self.history_1_vlayout.addWidget(
            self.image_label_1, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.pred_label_1 = QtWidgets.QLabel(DetectDialog)
        self.pred_label_1.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.pred_label_1.setText("")
        self.pred_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_label_1.setObjectName("pred_label_1")
        self.history_1_vlayout.addWidget(self.pred_label_1)
        self.conf_label_1 = QtWidgets.QLabel(DetectDialog)
        self.conf_label_1.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.conf_label_1.setText("")
        self.conf_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_label_1.setObjectName("conf_label_1")
        self.history_1_vlayout.addWidget(self.conf_label_1)
        self.sec_label_1 = QtWidgets.QLabel(DetectDialog)
        self.sec_label_1.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.sec_label_1.setText("")
        self.sec_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sec_label_1.setObjectName("sec_label_1")
        self.history_1_vlayout.addWidget(self.sec_label_1)
        self.history_hlayout.addLayout(self.history_1_vlayout)
        self.history_2_vlayout = QtWidgets.QVBoxLayout()
        self.history_2_vlayout.setObjectName("history_2_vlayout")
        self.image_label_2 = QtWidgets.QLabel(DetectDialog)
        self.image_label_2.setMinimumSize(QtCore.QSize(150, 150))
        self.image_label_2.setMaximumSize(QtCore.QSize(150, 150))
        self.image_label_2.setStyleSheet(
            "\n"
            'QLabel[is_hidden="false"]{\n'
            "border: 3px solid #cfab2d;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 3px solid #2a292e;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.image_label_2.setText("")
        self.image_label_2.setObjectName("image_label_2")
        self.history_2_vlayout.addWidget(
            self.image_label_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.pred_label_2 = QtWidgets.QLabel(DetectDialog)
        self.pred_label_2.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.pred_label_2.setText("")
        self.pred_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_label_2.setObjectName("pred_label_2")
        self.history_2_vlayout.addWidget(self.pred_label_2)
        self.conf_label_2 = QtWidgets.QLabel(DetectDialog)
        self.conf_label_2.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.conf_label_2.setText("")
        self.conf_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_label_2.setObjectName("conf_label_2")
        self.history_2_vlayout.addWidget(self.conf_label_2)
        self.sec_label_2 = QtWidgets.QLabel(DetectDialog)
        self.sec_label_2.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.sec_label_2.setText("")
        self.sec_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sec_label_2.setObjectName("sec_label_2")
        self.history_2_vlayout.addWidget(self.sec_label_2)
        self.history_hlayout.addLayout(self.history_2_vlayout)
        self.history_3_vlayout = QtWidgets.QVBoxLayout()
        self.history_3_vlayout.setObjectName("history_3_vlayout")
        self.image_label_3 = QtWidgets.QLabel(DetectDialog)
        self.image_label_3.setMinimumSize(QtCore.QSize(150, 150))
        self.image_label_3.setMaximumSize(QtCore.QSize(150, 150))
        self.image_label_3.setStyleSheet(
            "\n"
            'QLabel[is_hidden="false"]{\n'
            "border: 3px solid #cfab2d;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 3px solid #2a292e;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.image_label_3.setText("")
        self.image_label_3.setObjectName("image_label_3")
        self.history_3_vlayout.addWidget(
            self.image_label_3, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.pred_label_3 = QtWidgets.QLabel(DetectDialog)
        self.pred_label_3.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.pred_label_3.setText("")
        self.pred_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_label_3.setObjectName("pred_label_3")
        self.history_3_vlayout.addWidget(self.pred_label_3)
        self.conf_label_3 = QtWidgets.QLabel(DetectDialog)
        self.conf_label_3.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.conf_label_3.setText("")
        self.conf_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_label_3.setObjectName("conf_label_3")
        self.history_3_vlayout.addWidget(self.conf_label_3)
        self.sec_label_3 = QtWidgets.QLabel(DetectDialog)
        self.sec_label_3.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.sec_label_3.setText("")
        self.sec_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.sec_label_3.setObjectName("sec_label_3")
        self.history_3_vlayout.addWidget(self.sec_label_3)
        self.history_hlayout.addLayout(self.history_3_vlayout)
        self.history_4_vlayout = QtWidgets.QVBoxLayout()
        self.history_4_vlayout.setObjectName("history_4_vlayout")
        self.image_label_4 = QtWidgets.QLabel(DetectDialog)
        self.image_label_4.setMinimumSize(QtCore.QSize(150, 150))
        self.image_label_4.setMaximumSize(QtCore.QSize(150, 150))
        self.image_label_4.setStyleSheet(
            "\n"
            'QLabel[is_hidden="false"]{\n'
            "border: 3px solid #cfab2d;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 3px solid #2a292e;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.image_label_4.setText("")
        self.image_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label_4.setObjectName("image_label_4")
        self.history_4_vlayout.addWidget(
            self.image_label_4, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.pred_label_4 = QtWidgets.QLabel(DetectDialog)
        self.pred_label_4.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.pred_label_4.setText("")
        self.pred_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_label_4.setObjectName("pred_label_4")
        self.history_4_vlayout.addWidget(self.pred_label_4)
        self.conf_label_4 = QtWidgets.QLabel(DetectDialog)
        self.conf_label_4.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.conf_label_4.setText("")
        self.conf_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_label_4.setObjectName("conf_label_4")
        self.history_4_vlayout.addWidget(self.conf_label_4)
        self.sec_label_4 = QtWidgets.QLabel(DetectDialog)
        self.sec_label_4.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.sec_label_4.setText("")
        self.sec_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.sec_label_4.setObjectName("sec_label_4")
        self.history_4_vlayout.addWidget(self.sec_label_4)
        self.history_hlayout.addLayout(self.history_4_vlayout)
        self.history_5_vlayout = QtWidgets.QVBoxLayout()
        self.history_5_vlayout.setObjectName("history_5_vlayout")
        self.image_label_5 = QtWidgets.QLabel(DetectDialog)
        self.image_label_5.setMinimumSize(QtCore.QSize(150, 150))
        self.image_label_5.setMaximumSize(QtCore.QSize(150, 150))
        self.image_label_5.setStyleSheet(
            "\n"
            'QLabel[is_hidden="false"]{\n'
            "border: 3px solid #cfab2d;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 3px solid #2a292e;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.image_label_5.setText("")
        self.image_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label_5.setObjectName("image_label_5")
        self.history_5_vlayout.addWidget(
            self.image_label_5, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.pred_label_5 = QtWidgets.QLabel(DetectDialog)
        self.pred_label_5.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.pred_label_5.setText("")
        self.pred_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_label_5.setObjectName("pred_label_5")
        self.history_5_vlayout.addWidget(self.pred_label_5)
        self.conf_label_5 = QtWidgets.QLabel(DetectDialog)
        self.conf_label_5.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.conf_label_5.setText("")
        self.conf_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_label_5.setObjectName("conf_label_5")
        self.history_5_vlayout.addWidget(self.conf_label_5)
        self.sec_label_5 = QtWidgets.QLabel(DetectDialog)
        self.sec_label_5.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "border: 1px solid #cfab2d;\n"
            "font-family:sans-serif;\n"
            "color: #cfab2d;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "border: 1px solid #2a292e;\n"
            "font-family:sans-serif;\n"
            "color: #2a292e;\n"
            "font-size: 10px;\n"
            "text-align: center;\n"
            "border-radius: 5px;\n"
            "font-weight: bold;\n"
            "font-family: sans-serif;\n"
            "text-transform: uppercase;\n"
            "letter-spacing: 0.1em;\n"
            "}\n"
            ""
        )
        self.sec_label_5.setText("")
        self.sec_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.sec_label_5.setObjectName("sec_label_5")
        self.history_5_vlayout.addWidget(self.sec_label_5)
        self.history_hlayout.addLayout(self.history_5_vlayout)
        self.main_vlayout.addLayout(self.history_hlayout)
        self.horizontalLayout_9.addLayout(self.main_vlayout)

        self.retranslateUi(DetectDialog)
        QtCore.QMetaObject.connectSlotsByName(DetectDialog)

    def retranslateUi(self, DetectDialog):
        _translate = QtCore.QCoreApplication.translate
        DetectDialog.setWindowTitle(_translate("DetectDialog", "Dialog"))
        self.title_label.setText(_translate("DetectDialog", "MASK DETECTION"))
        self.detect_again_button.setText(_translate("DetectDialog", "DETECT AGAIN"))
        self.back_button.setText(_translate("DetectDialog", "BACK"))
