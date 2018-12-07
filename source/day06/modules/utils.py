import numpy as np


class Utils:

    def get_np_coords(filepath):
        coords = np.loadtxt(filepath, dtype=int, delimiter=', ')
        return coords

    def get_lines(filepath):

        lines = []
        with open(filepath) as f:
            while True:
                line = f.readline().strip('\n')
                if line != '':
                    lines.append(line)
                else:
                    break

        return lines

    def get_coords(lines):

        coords = []
        for line in lines:
            coords_tuple = line.split(', ')
            coord = (int(coords_tuple[0]), int(coords_tuple[1]))
            coords.append(coord)

        return coords
