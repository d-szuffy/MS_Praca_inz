from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        self.canvas.graph = self.canvas.figure.add_subplot(111, xlim=(0, 150))
        self.setLayout(vertical_layout)


# returns True if the point is above functions and returns False when opposite
def check_if_the_point_is_above_function(point, m, c):
    if point[1] > m * point[0] + c:
        return True
    else:
        return False


def find_cross_point_of_two_functions(m1, c1, m2, c2):
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return x, y
