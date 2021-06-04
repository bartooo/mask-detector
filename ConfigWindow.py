from PyQt5.QtWidgets import QDialog
class ConfigWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self._initUI()
        self.show()
    
    def _initUI(self):
        self.resize(900, 600)

