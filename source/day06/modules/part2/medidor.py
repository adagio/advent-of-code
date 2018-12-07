import numpy as np
from collections import defaultdict


class Medidor:

    def __init__(self, coords, cota):
        self.coords = coords
        self.grid = self.__get_grid(coords)
        self.cota = cota

    def __get_grid(self, coords):
        x_min, y_min = coords.min(axis=0)  # - 1
        x_max, y_max = coords.max(axis=0)  # + 2

        py, px = np.mgrid[x_min:x_max, y_min:y_max]

        px_ravel = px.ravel()
        py_ravel = py.ravel()

        grid = np.c_[py_ravel, px_ravel]

        return grid

    def __get_distance_sum(self, point):
        distance_sum = 0
        p_x, p_y = point
        for coord in self.coords:
            coord_x, coord_y = coord
            distance_to_coord = abs(p_x - coord_x) + abs(p_y - coord_y)
            distance_sum += distance_to_coord
            if distance_sum > self.cota:
                break
        return distance_sum

    def get_largest_area(self):

        area = []

        for point in self.grid:
            distance_sum = self.__get_distance_sum(point)

            if distance_sum < self.cota:
                area.append(distance_sum)

        return area

