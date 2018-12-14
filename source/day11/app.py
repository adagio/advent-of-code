from modules.power_level import PowerLevel


serial = 7403

"""
power_tests = {
    # serial, x, y: power level
    ( 8, (  3,   5)): 4,
    (57, (122,  79)): -5,
    (39, (217, 196)): 0,
    (71, (101, 153)): 4,
}


for (tserial, cell), expected in power_tests.items():
    # indexing a [y, x] arranged matrix with 0-based offsets
    x, y = cell
    powerLevel = PowerLevel(tserial)
    power_level_grid = powerLevel.get_power_level_grid()
    cell_power_level = power_level_grid[x - 1, y - 1]
    print(cell_power_level)
    #assert gp == expected

max_tests = {
    18: (33, 45),
    42: (21, 61),
}

for tserial, expected in max_tests.items():
    powerLevel = PowerLevel(tserial)
    mg = powerLevel.max_grid()
    print(f'{mg}')
    # assert mg == expected
"""

powerLevel = PowerLevel(serial)
powerLevel.max_grid()

