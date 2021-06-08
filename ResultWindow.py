from PyQt5.QtWidgets import QDialog, QDesktopWidget, QMainWindow
from ResultWindowUI import Ui_ResultWindow
from PyQt5 import QtCore
import webbrowser
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.Qt import QCursor
from PyQt5.QtCore import QUrl


class ResultWindow(QMainWindow, Ui_ResultWindow):
    def __init__(self, result, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.result = result
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.setup_gui()
        self.center()
        self.position = self.pos()
        self.setup_cursors()
        self.setup_buttons()
        self.setWindowTitle("DETECTION RESULT")
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setup_cursors(self):
        self.button_buy_mask.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_read_restrictions.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def setup_buttons(self):
        self.button_buy_mask.clicked.connect(self._on_buy_clicked)
        self.button_read_restrictions.clicked.connect(self._on_read_clicked)

    def _on_buy_clicked(self):
        webbrowser.open(
            "http://allegro.pl/listing?string=maseczki&bmatch=e2101-d3794-c3683-hea-1-4-0528"
        )

    def _on_read_clicked(self):
        webbrowser.open(
            "https://www.gov.pl/web/koronawirus/aktualne-zasady-i-ograniczenia"
        )

    def setup_gui(self):
        self.result_label.setText(self.result)
        self.mediaPlayer.setVideoOutput(self.video_widget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("ui/video.mp4")))
        self.mediaPlayer.play()

    def closeEvent(self, event):
        self.mediaPlayer.pause()
