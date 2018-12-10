from parse import parse
import numpy as np

filename = 'input1'
filepath = f'data/{filename}.plain'

positions = []
velocities = []

pattern = 'position=<{px},{py}> velocity=<{vx},{vy}>'

for line in open(filepath):
    result = parse(pattern, line)
    position = (int(result['px']), int(result['py']))
    positions.append(position)
    velocity = (int(result['vx']), int(result['vy']))
    velocities.append(velocity)

np_positions = np.array(positions, dtype=tuple)
np_velocities = np.array(velocities, dtype=tuple)
# print(np_positions)
# new_positions = np_positions + np_velocities

def draw():
    x_min, y_min = np_positions.min(axis=0)
    x_max, y_max = np_positions.max(axis=0)
    for y in range(y_min, y_max + 1):
        line = ''
        for x in range(x_min, x_max + 1):
            if [x, y] in np_positions.tolist():
                line += '#'
            else:
                line += '.'
        print(line)

draw()

