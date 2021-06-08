# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 810)
        MainWindow.setStyleSheet(
            "QWidget #main_h_layout{\n"
            "    color: #cfab2d;\n"
            "    background-color: #2a292e;\n"
            "    border: 3px solid #cfab2d;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.main_h_layout = QtWidgets.QWidget(MainWindow)
        self.main_h_layout.setObjectName("main_h_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_h_layout)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_v_layout = QtWidgets.QVBoxLayout()
        self.menu_v_layout.setObjectName("menu_v_layout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.menu_v_layout.addItem(spacerItem)
        self.logo_label = QtWidgets.QLabel(self.main_h_layout)
        self.logo_label.setMinimumSize(QtCore.QSize(600, 600))
        self.logo_label.setMaximumSize(QtCore.QSize(600, 600))
        self.logo_label.setStyleSheet("*{}")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.menu_v_layout.addWidget(
            self.logo_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.menu_v_layout.addItem(spacerItem1)
        self.button_warning_vlayout = QtWidgets.QVBoxLayout()
        self.button_warning_vlayout.setSpacing(0)
        self.button_warning_vlayout.setObjectName("button_warning_vlayout")
        self.button_run_detector = QtWidgets.QPushButton(self.main_h_layout)
        self.button_run_detector.setStyleSheet(
            "QPushButton{\n"
            "    color: #cfab2d;\n"
            "    background-color: #2a292e;\n"
            "    text-align: center;\n"
            "    max-width: 33em;\n"
            "    width: 12em;\n"
            "    font-size: 16px;\n"
            "    height: 3em;\n"
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
        self.button_run_detector.setObjectName("button_run_detector")
        self.button_warning_vlayout.addWidget(
            self.button_run_detector, 0, QtCore.Qt.AlignHCenter
        )
        self.warning_label = QtWidgets.QLabel(self.main_h_layout)
        self.warning_label.setStyleSheet(
            'QLabel[is_hidden="false"]{\n'
            "    color: #cfab2d;\n"
            "    min-height: 15px;\n"
            "    max-height: 15px;\n"
            "    font-family: sans-serif;\n"
            "    font-size: 9px;\n"
            "    font-style: italic;\n"
            "    text-transform: uppercase;\n"
            "    letter-spacing: 0.1em;\n"
            "\n"
            "}\n"
            'QLabel[is_hidden="true"]{\n'
            "    color: #2a292e;\n"
            "    min-height: 15px;\n"
            "    max-height: 15px;\n"
            "    font-family: sans-serif;\n"
            "    font-style: italic;\n"
            "    font-size: 9px;\n"
            "    text-transform: uppercase;\n"
            "    letter-spacing: 0.1em;\n"
            "}"
        )
        self.warning_label.setText("")
        self.warning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_label.setObjectName("warning_label")
        self.button_warning_vlayout.addWidget(
            self.warning_label, 0, QtCore.Qt.AlignHCenter
        )
        self.menu_v_layout.addLayout(self.button_warning_vlayout)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.menu_v_layout.addItem(spacerItem2)
        self.button_config = QtWidgets.QPushButton(self.main_h_layout)
        self.button_config.setStyleSheet(
            "QPushButton{\n"
            "    color: #cfab2d;\n"
            "    background-color: #2a292e;\n"
            "    text-align: center;\n"
            "    max-width: 33em;\n"
            "    width: 12em;\n"
            "    font-size: 16px;\n"
            "    height: 3em;\n"
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
        self.button_config.setObjectName("button_config")
        self.menu_v_layout.addWidget(self.button_config, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.menu_v_layout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.menu_v_layout)
        MainWindow.setCentralWidget(self.main_h_layout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "REAL-TIME FACE MASK DETECTOR")
        )
        self.button_run_detector.setText(_translate("MainWindow", "START DETECTION"))
        self.button_config.setText(_translate("MainWindow", "SETTINGS"))
