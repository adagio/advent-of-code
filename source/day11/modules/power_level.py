import numpy as np
from numpy.lib.stride_tricks import as_strided


class PowerLevel:

    def __init__(self, serial, gridsize):
        self.serial = serial
        self.GRIDSIZE = gridsize

    def get_power_level(self, x, y):
        rack_id = (x + 1) + 10
        power_level = rack_id * (y + 1)
        power_level += self.serial
        power_level *= rack_id
        hundreds_number = power_level // 100  # floor division
        hundreds_digit = hundreds_number % 10
        power_level = hundreds_digit - 5
        return power_level

    def __get_power_level_grid(self):
        grid = np.fromfunction(
            self.get_power_level,
            (self.GRIDSIZE, self.GRIDSIZE)
        )
        return grid

    def __summed_grid_powers(self, power_levels, window_size=3):
        GRIDSIZE = self.GRIDSIZE
        window_count = GRIDSIZE - window_size + 1
        shape = (window_count, window_count, window_size, window_size)
        strides = power_levels.strides * 2
        return as_strided(power_levels, shape, strides).sum(axis=(2, 3))
        
    def max_grid(self, window_size=3):
        summed = self.__summed_grid_powers(
            self.__get_power_level_grid(),
            window_size = window_size
        )
        y, x = np.unravel_index(summed.argmax(), summed.shape)
        return x + 1, y + 1

    def d_optimal_window_size(self):
        GRIDSIZE = self.GRIDSIZE
        power_levels = self.__get_power_level_grid()
        by_size = np.stack([
            np.pad(self.__summed_grid_powers(power_levels, i + 1), (0, i), 'constant')
            for i in range(GRIDSIZE)
        ]).reshape(GRIDSIZE, -1)
        size = by_size.max(axis=1).argmax()
        y, x = np.unravel_index(by_size[size].argmax(), power_levels.shape)
        return x + 1, y + 1, size + 1    

    def optimal_window_size(self):
        GRIDSIZE = self.GRIDSIZE
        power = self.__get_power_level_grid()
        summed = np.copy(power)
        best_size = 1
        highest_power = summed.max()
        best_pos = summed.argmax()
        # updated sums for rows and columns to update the current size with
        power_rolled = rowsums = colsums = power

        power_levels = []

        for size in range(2, GRIDSIZE + 1):
            # matrix to update our running row and column sums;
            # roll up and left, and clear the last row and column
            power_rolled = np.roll(power_rolled, (-1, -1), (0, 1))
            power_rolled[-1, :] = 0
            power_rolled[:, -1] = 0
            # roll rowsums up, clear last row and add power_rolled values
            # Then add these to our summed windows
            rowsums = np.roll(rowsums, -1, 0)
            rowsums[-1, :] = 0
            rowsums += power_rolled
            summed += rowsums
            # roll the column sums to the left, add these to the summed
            # windows first, then add power_rolled to the column sums.
            colsums = np.roll(colsums, -1, 1)
            colsums[:, -1] = 0
            summed += colsums
            colsums += power_rolled
            # finally, clear the next inner row and column of summed
            summed[-(size - 1):, :] = 0
            summed[:, -(size - 1):] = 0
            
            # now our summed matrix is up to date for this window size. Check if it
            # has a larger power output
            power_output = summed.max()
            power_levels.append(power_output)
            
            if power_output > highest_power:
                highest_power = power_output
                best_size = size
                best_pos = summed.argmax()

        y, x = np.unravel_index(best_pos, summed.shape)
        return x + 1, y + 1, best_size


    def show_max_power_level(self):
        """
        by width grid
        """
        matrix = self.__get_power_level_grid()
        from pprint import pprint
        MATRIXSIZE = self.GRIDSIZE
        min_window_size = 3
        for width in range(min_window_size, MATRIXSIZE + 1):
            windows_sums = sum(
                matrix[
                    j:j-width+1 or None,
                    i:i-width+1 or None
                ]
                for i in range(0, width)
                for j in range(0, width)
            )
            max_sum = int(windows_sums.max())
            position = np.where(windows_sums == max_sum)
            px = position[0][0]
            py = position[1][0]

        print(f'width: {width}, max_sum: {max_sum}, position: {px+1},{py+1}\n')
            
