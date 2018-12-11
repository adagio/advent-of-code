import numpy as np


def gen_area(iterations, positions_nda, velocities_nda):
    """
    Given iterations, positions and velocities
    Return area. Area is a dimension (w*h)
    """
    positions = positions_nda + velocities_nda * iterations
    x_min, y_min = positions.min(axis=0)
    x_max, y_max = positions.max(axis=0)
    w = x_max - x_min
    h = y_max - y_min
    area = w * h
    return area

