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

positions_nda = np.array(positions, dtype=tuple)
velocities_nda = np.array(velocities, dtype=tuple)

x_min, y_min = positions_nda.min(axis=0)
x_max, y_max = positions_nda.max(axis=0)

def draw(positions_nda):
    for y in range(y_min, y_max + 1):
        line = ''
        for x in range(x_min, x_max + 1):
            if [x, y] in positions_nda.tolist():
                line += '#'
            else:
                line += '.'
        print(line)

iterations = 4
for i in range(iterations):
    print(f'Iteration: {i}')
    draw(positions_nda)
    positions_nda += velocities_nda

