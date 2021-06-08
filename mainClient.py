import sys
from ClientDetector.MainWindow import MainWindow, get_logging_param
from PyQt5.Qt import QApplication


def client_main():
    logging_param = None
    try:
        logging_param = get_logging_param(sys.argv)
    except Exception as e:
        print(e)
        return
    app = QApplication([])
    window = MainWindow(logging_param)
    sys.exit(app.exec_())


if __name__ == "__main__":
    client_main()
