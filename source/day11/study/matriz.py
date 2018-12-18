import numpy as np


class Matriz:

    def __init__(self, gridsize):
        self.GRIDSIZE = gridsize

    def get_box_value(self, x, y):
        value = (x * self.GRIDSIZE) + 1 + y
        return value

    def get_grid(self):
        grid = np.fromfunction(
            self.get_box_value,
            (self.GRIDSIZE, self.GRIDSIZE)
        )
        return grid

    def show_windows(self):
        grid = self.get_grid()
        
        from pprint import pprint
        pprint(grid)

        GRIDSIZE = self.GRIDSIZE

        for width in range(3, GRIDSIZE + 1):          
            for x in range(GRIDSIZE - width + 1):
                for y in range(GRIDSIZE - width + 1):
                    window = grid[x:x+width, y:y+width]
                    if width == 3:
                        pprint(window)
#                        window_sum = sum(window)
#                        print(f'sum: {window_sum}')
"""
        for width in range(3, GRIDSIZE + 1):
            windows_sums = sum(
                grid[
                    x:x+width,
                    y:y+width
                ]
                for y in range(GRIDSIZE - width + 1)
                for x in range(GRIDSIZE - width + 1)
            )
            pprint(windows_sums)
            max_sum = int(windows_sums.max())
            location = np.where(windows_sums == max_sum)
            print(f'width: {width}, max_sum: {max_sum}, locatiion: {location[0][0] + 1}, {location[1][0] + 1}')
"""
