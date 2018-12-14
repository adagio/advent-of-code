import numpy as np


class PowerLevel:

    def __init__(self, serial):
        self.serial = serial
        self.GRIDSIZE = 300

    def get_power_level(self, x, y):
        rack_id = (x + 1) + 10
        power_level = rack_id * (y + 1)
        power_level += self.serial
        power_level *= rack_id
        hundreds_number = power_level // 100  # floor division
        hundreds_digit = hundreds_number % 10
        power_level = hundreds_digit - 5
        return power_level

    def get_power_level_grid(self):
        grid = np.fromfunction(
            self.get_power_level,
            (self.GRIDSIZE, self.GRIDSIZE)
        )
        return grid

    def max_grid(self):
        grid = self.get_power_level_grid()
        for width in range(3, self.GRIDSIZE):
            windows = sum(
                grid[
                    x:x-width+1 or None,
                    y:y-width+1 or None
                ]
                for x in range(width)
                for y in range(width)
            )
            maximum = int(windows.max())
            location = np.where(windows == maximum)
            print(width, maximum, location[0][0] + 1, location[1][0] + 1)

