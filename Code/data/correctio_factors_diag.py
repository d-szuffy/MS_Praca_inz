import matplotlib.pyplot as plt
from data.linear_functions import PointsForLinearFunctions
from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
#from matplotlib import pyplot as plt
# import numpy
# from PIL import Image
# from numpy import ones,vstack
# from numpy.linalg import lstsq



class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)


        self.canvas.kutas = self.canvas.figure.add_subplot(111, xlim=(0, 150))
        #self.canvas.axes = self.canvas.figure.add_axes(xlim=(0, 150))
        self.setLayout(vertical_layout)


# factors_diagram_img = Image.open(r'C:\Users\Mateusz.Szawczenko\Desktop\Praca inżynierska\MS_Praca_inz\Rysunki\Wykres wsp. korekcji.png')
#
# plt.imshow(factors_diagram_img)
# def get_straight_linear(point):
#     x_coords, y_coords = zip(*point)
#     a = vstack([x_coords, ones(len(x_coords))]).T
#     m, c = lstsq(a, y_coords, rcond=None)[0]
#     print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
#
#
# get_straight_linear([(0, 0.67), (70, 0.98)])
# LIST_OF_POINTS = PointsForLinearFunctions.LIST_OF_POINTS
# print(LIST_OF_POINTS)
#
# def draw_line_function_between_two_points(points):
#     i = 0.1
#     for points in LIST_OF_POINTS:
#
#         plt.axline(points[0], points[1], color=(i, 0.9-i, 0.8))
#         plt.xlim([10, 150])
#         plt.ylim([-0.5, 1])
#         i += 0.05
#         print(i)
#     plt.show()
#
#
# draw_line_function_between_two_points(LIST_OF_POINTS)

