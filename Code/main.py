import Gear_UI
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPropertyAnimation

WINDOW_SIZE = 0

class MyForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Gear_UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)


 # Button click events to our top bar buttons
        #
        #Minimize window
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        #Close window
        self.ui.close_btn.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        self.ui.restore_btn.clicked.connect(lambda: self.restore_or_maximize_window())

# Restore or maximize your window


        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # ###############################################
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            # ###############################################


        self.ui.main_header.mouseMoveEvent = moveWindow

        self.show()
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
        # ###############################################

    # ###############################################

    def restore_or_maximize_window(self):

# Global windows state
        global WINDOW_SIZE #The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
# If the window is not maximized
        	WINDOW_SIZE = 1
# Update value to show that the window has been maximized
        	self.showMaximized()
# Update button icon
# self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))#Show maximized icon
        else:
# If the window is on its default size
            WINDOW_SIZE = 0 #Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()
# Update button icon
# self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))#Show minized icon
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(App.exec())