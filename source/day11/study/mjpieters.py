from itertools import product
import numpy as np
from numpy.lib.stride_tricks import as_strided


# These values never change, so can be made globals
GRIDSIZE = 300
XX, YY = np.meshgrid(np.arange(1, GRIDSIZE + 1), np.arange(1, GRIDSIZE + 1))
RACK_ID = XX + 10


def grid_powers(serial):
    # calculate power levels
    return (RACK_ID * YY + serial) * RACK_ID // 100 % 10 - 5

def summed_grid_powers(power_levels, window_size=3):
    # sum levels for 3 x 3 subgrids; substitute edges for zeros
    
    window_count = GRIDSIZE - window_size + 1
    # output shape, 2d grid of 2d windows
    shape = (window_count, window_count, window_size, window_size)
    # per shape axis, the stride across power_levels matches up to the
    # same axes.
    strides = power_levels.strides * 2

    # we want to sum every subwindow, so it is time to start striding
    # we need to produce a (window_count, window_count, window_size, window_size)
    # matrix that then is summed on the last 2 axes.
    return as_strided(power_levels, shape, strides).sum(axis=(2, 3))
    
def max_grid(serial):    
    summed = summed_grid_powers(grid_powers(serial))

    # produce the (x, y) coordinates for the largest 3x3 grid top-left coordinate
    # argmax() flattens the array and gives us an index based on that, so we need
    # numpy.unravel to give back the original y, x coordinates.
    y, x = np.unravel_index(summed.argmax(), summed.shape)
    # Translate from zero to one-based indexing
    return x + 1, y + 1

