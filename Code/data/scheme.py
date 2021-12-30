from PyQt5.QtWidgets import*


from PyQt5.QtOpenGL import QGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from data.results import Result


class GLPlotWidget(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(800, 640)

    def paintGL(self):
        print("paintGL działa")
        if Result.pinion_pitch_diameter is None or Result.second_wheel_pitch_diameter is None:
            ratio = 1
        else:
            ratio = Result.second_wheel_pitch_diameter / Result.pinion_pitch_diameter
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-1.75, 0.5, -6.0)
        # glPolygonMode(GL_FRONT, GL_FILL)
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        self.draw_wheels(1, ratio)

        glEnd()
        glFlush()

    def draw_wheels(self, sum_of_diameters, ratio):

        d_1 = sum_of_diameters / (ratio + 1)
        d_2 = d_1 * ratio

        #print(d_1, d_2)
        # pinion
        glVertex2f(0.3, 0.125)
        glVertex2f(0.3, 0.125 - d_1)
        #glVertex2f(0.3, -0.125)
        #glVertex2f(0.3, -0.425)
        glVertex2f(0.275, 0.125)
        glVertex2f(0.325, 0.125)
        glVertex2f(0.275, 0.125 - d_1)
        glVertex2f(0.325, 0.125 - d_1)

        # wheel

        glVertex2f(0.3, 0.125)
        glVertex2f(0.3, 0.125 - d_1 - d_2)
        glVertex2f(0.275, 0.125 - d_1 - d_2)
        glVertex2f(0.325, 0.125 - d_1 - d_2)

        pinion_shaft_y , wheel_shaft_y = 0.125 - (d_1/2), 0.125 - d_1 - (d_2/2)

        self.draw_shafts(pinion_shaft_y, wheel_shaft_y)
        self.draw_cover(pinion_shaft_y, wheel_shaft_y, sum_of_diameters)
        self.draw_clutch(pinion_shaft_y, wheel_shaft_y)
        self.draw_machines(pinion_shaft_y, wheel_shaft_y)

    def draw_shafts(self, pinion_shaft_y, wheel_shaft_y):

        glVertex2f(-0.25, pinion_shaft_y)
        glVertex2f(0.6, pinion_shaft_y)

        glVertex2f(0, wheel_shaft_y)
        glVertex2f(0.8, wheel_shaft_y)

        self.pair_of_rectangles_without_edges([0, pinion_shaft_y + 0.125], [0.1, pinion_shaft_y + 0.025])
        self.pair_of_rectangles_without_edges([0.5, pinion_shaft_y + 0.125], [0.6, pinion_shaft_y + 0.025])
        self.pair_of_rectangles_without_edges([0, wheel_shaft_y + 0.125], [0.1, wheel_shaft_y + 0.025])
        self.pair_of_rectangles_without_edges([0.5, wheel_shaft_y + 0.125], [0.6, wheel_shaft_y + 0.025])


    def draw_cover(self, pinion_shaft_y, wheel_shaft_y, sum_of_diameters):
        self.rectangle_without_one_edge([0.05, 0.125 + 0.175], [0.55, pinion_shaft_y + 0.025], 'bottom')
        self.rectangle_without_one_edge([0.05, wheel_shaft_y - 0.025], [0.55, 0.125 - sum_of_diameters - 0.175], 'top')
        glVertex2f(0.05, pinion_shaft_y - 0.025)
        glVertex2f(0.05, wheel_shaft_y + 0.025)
        glVertex2f(0.55, pinion_shaft_y - 0.025)
        glVertex2f(0.55, wheel_shaft_y + 0.025)

    def draw_clutch(self, pinion_shaft_y, wheel_shaft_y):
        self.rectangle_without_one_edge([-0.32, pinion_shaft_y + 0.1], [-0.25, pinion_shaft_y - 0.1], 'left')
        self.rectangle_without_one_edge([0.8, wheel_shaft_y + 0.1], [0.87, wheel_shaft_y - 0.1], 'right')

        glVertex2f(-0.27, pinion_shaft_y)
        glVertex2f(-0.55, pinion_shaft_y)

        glVertex2f(-0.27, pinion_shaft_y + 0.05)
        glVertex2f(-0.27, pinion_shaft_y - 0.05)

        glVertex2f(0.82, wheel_shaft_y)
        glVertex2f(1.1, wheel_shaft_y)

        glVertex2f(0.82, wheel_shaft_y + 0.05)
        glVertex2f(0.82, wheel_shaft_y - 0.05)

    def draw_machines(self, pinion_shaft_y, wheel_shaft_y):
        self.rectangle_without_one_edge([-1.15, pinion_shaft_y + 0.3], [-0.55, pinion_shaft_y - 0.3])
        glVertex2f(-1.15, pinion_shaft_y + 0.3)
        glVertex2f(-0.55, pinion_shaft_y - 0.3)
        glVertex2f(-1.15, pinion_shaft_y - 0.3)
        glVertex2f(-0.55, pinion_shaft_y + 0.3)

        self.rectangle_without_one_edge([1.1, wheel_shaft_y + 0.3], [1.7, wheel_shaft_y - 0.3])
        glVertex2f(1.1, wheel_shaft_y + 0.3)
        glVertex2f(1.7, wheel_shaft_y - 0.3)
        glVertex2f(1.1, wheel_shaft_y - 0.3)
        glVertex2f(1.7, wheel_shaft_y + 0.3)

        glVertex2f(-0.85, pinion_shaft_y + 0.325)
        glVertex2f(-1, 1.55)

        glVertex2f(1.4, wheel_shaft_y + 0.325)
        glVertex2f(1.25, 1.55)

    def pair_of_rectangles_without_edges(self, left_upper_vertex, right_lower_vertex):
        #print(left_upper_vertex, right_lower_vertex)
        self.rectangle_without_one_edge([left_upper_vertex[0], left_upper_vertex[1]], [right_lower_vertex[0], right_lower_vertex[1]], 'top')
        self.rectangle_without_one_edge([left_upper_vertex[0], left_upper_vertex[1] - 0.15], [right_lower_vertex[0], right_lower_vertex[1] - 0.15], 'bottom')

    def rectangle_without_one_edge(self, left_upper_vertex, right_lower_vertex, missing_edge=None):

        if missing_edge is None:
            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])
            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])

        elif missing_edge == "top":

            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])


        elif missing_edge == "bottom":

            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])
            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])

        elif missing_edge == "left":


            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])


        elif missing_edge == "right":


            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(right_lower_vertex[0], left_upper_vertex[1])
            glVertex2f(left_upper_vertex[0], left_upper_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])
            glVertex2f(left_upper_vertex[0], right_lower_vertex[1])
            glVertex2f(right_lower_vertex[0], right_lower_vertex[1])


    def initializeGL(self):
        glClearColor(255, 255, 255, 255)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.33, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)


# define a Qt window with an OpenGL widget inside it

