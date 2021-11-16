from data.linear_functions import *
from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib import pyplot as plt
import numpy as np
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
        # self.canvas.axes = self.canvas.figure.add_axes(xlim=(0, 150))
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


# returns True if the point is above functions and returns False when opposite
def check_if_the_point_is_above_function(point, m, c):
    if point[1] > m * point[0] + c:
        # draw_line_function_based_on_m_and_c(m, c, 'green')
        return True
    else:
        # draw_line_function_based_on_m_and_c(m, c, 'red')
        return False


# # draws each linear function on plot
# def draw_line_function_based_on_m_and_c(m, c, linecolor):
#     x = np.linspace(-500, 500, 1000)
#     y = m * x + c
#     plt.plot(x, y, color=linecolor, label=f'y={m.round(3)}x+{c.round(2)}1')
#

def find_cross_point_of_two_functions(m1, c1, m2, c2):
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return x, y
#
#
# def draw_function_with_point_given_point_and_cross_point():
#     pass
#
#
# # constant with previously defined points.
# LIST_OF_POINTS = PointsForLinearFunctions.LIST_OF_POINTS
# LIST_OF_FUNCTIONS = []
# GIVEN_POINT = [75, 0.4]
#
# # creating linear functions represented by y = mx + c from the list of points each of them consist of
# for point in LIST_OF_POINTS:
#     function = get_straight_linear(point)
#     LIST_OF_FUNCTIONS.append(function)
#
# # constants which help to indentify function we search for
# indexes_of_functions_above_given_point = []
# indexes_of_functions_below_given_point = []
# function_below_given_point = []
# function_above_given_point = []
#
# # iterate through list of functions to check whether it is below or above the given point and draw all functions on plot
# for i in range(0, len(LIST_OF_FUNCTIONS)):
#     draw_line_function_based_on_m_and_c(LIST_OF_FUNCTIONS[i][0], LIST_OF_FUNCTIONS[i][1], 'blue')
#     is_above_function = check_if_the_point_is_above_function(GIVEN_POINT, LIST_OF_FUNCTIONS[i][0], LIST_OF_FUNCTIONS[i][1])
#     if is_above_function:
#         indexes_of_functions_below_given_point.append(i)
#     else:
#         indexes_of_functions_above_given_point.append(i)
#
# # get the functions which are right above and right below the given point from lists of functions
# function_above_given_point = indexes_of_functions_above_given_point[0]
# function_below_given_point = indexes_of_functions_below_given_point[-1]
#
# # overdraw functions right above and right below the given point with different color
# draw_line_function_based_on_m_and_c(LIST_OF_FUNCTIONS[function_above_given_point][0], LIST_OF_FUNCTIONS[function_above_given_point][1], 'green')
# draw_line_function_based_on_m_and_c(LIST_OF_FUNCTIONS[function_below_given_point][0], LIST_OF_FUNCTIONS[function_below_given_point][1], 'green')
# cross_point_x, cross_point_y = find_cross_point_of_two_functions(LIST_OF_FUNCTIONS[function_above_given_point][0],
#                                                                  LIST_OF_FUNCTIONS[function_above_given_point][1],
#                                                                  LIST_OF_FUNCTIONS[function_below_given_point][0],
#                                                                  LIST_OF_FUNCTIONS[function_below_given_point][1])
# created_linear_func = get_straight_linear([(cross_point_x, cross_point_y), (GIVEN_POINT[0], GIVEN_POINT[1])])
# searched_correction_factor = created_linear_func[0] * 20 + created_linear_func[1]
#
# # plot settings
# plt.xlabel('x')
# plt.ylabel('y')
# # plt.legend(loc='lower left')
# plt.xlim(-50, 150)
# plt.ylim(-0.5, 1)
# plt.plot(GIVEN_POINT[0], GIVEN_POINT[1], marker='o', markersize=5, markerfacecolor="red")
# plt.plot(cross_point_x, cross_point_y, marker='o', markersize=5, markerfacecolor="red")
# plt.plot(20, searched_correction_factor, marker='o', markersize=5, markerfacecolor="red")
# plt.plot([20, 20], [-0.5, searched_correction_factor], linestyle='dashed')
# plt.plot([20, -50], [searched_correction_factor, searched_correction_factor], linestyle='dashed')
# plt.axline([cross_point_x, cross_point_y], [GIVEN_POINT[0], GIVEN_POINT[1]])
# plt.annotate(f'x1 = {round(searched_correction_factor, 3)}', xy=(-50, searched_correction_factor),
#              xytext=(0, searched_correction_factor), textcoords=plt.gca().get_yaxis_transform(),
#              va='center', ha='right')
# plt.show()
# print(plt)
