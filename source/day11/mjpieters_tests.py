import numpy as np

from study.mjpieters import grid_powers
from study.mjpieters import max_grid


power_tests = {
    # serial, x, y: power level
    ( 8, (  3,   5)): 4,
    (57, (122,  79)): -5,
    (39, (217, 196)): 0,
    (71, (101, 153)): 4,
}

print('power tests')
for (tserial, cell), expected in power_tests.items():
    # indexing a [y, x] arranged matrix with 0-based offsets
    x, y = cell
    gp = grid_powers(tserial)[y - 1, x- 1]
    print(gp)
    assert gp == expected

max_tests = {
    18: (33, 45),
    42: (21, 61),
}

print('max tests')
for tserial, expected in max_tests.items():
    mg = max_grid(tserial)
    print(f'{mg}')
    assert mg == expected

serial = 7403
mg = max_grid(serial)
print(f'{mg}')

