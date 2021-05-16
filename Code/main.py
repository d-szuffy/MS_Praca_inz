import Gear_UI
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPropertyAnimation


class MyForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Gear_UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(App.exec())