from numpy import ones, vstack
from numpy.linalg import lstsq


class PointsForLinearFunctions(object):
    R17 = [(0, 0.67), (75, 1)]
    R16 = [(0, 0.61), (134, 1)]
    R15 = [(0, 0.55), (150, 0.76)]
    R14 = [(0, 0.5), (150, 0.5)]
    R13 = [(0, 0.45), (150, 0.185)]
    R12 = [(0, 0.405), (150, -0.15)]
    R11 = [(0, 0.38), (150, -0.42)]
    R10 = [(0, 0.365), (116, -0.5)]
    R9 = [(0, 0.357), (87.2, -0.5)]
    R8 = [(0, 0.35), (69, -0.5)]
    R7 = [(0, 0.365), (57.3, -0.5)]
    R6 = [(0, 0.385), (45, -0.42)]
    R5 = [(0, 0.425), (35.5, -0.36)]
    R4 = [(0, 0.447), (31.5, -0.325)]
    R3 = [(0, 0.455), (27.5, -0.314)]
    R2 = [(0, 0.44), (25.5, -0.3)]
    LIST_OF_POINTS = [R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17]


def get_straight_linear(points):
    x_coords, y_coords = zip(*points)
    a = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(a, y_coords, rcond=None)[0]
    return m, c
