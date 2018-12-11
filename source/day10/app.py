from parse import parse
import numpy as np
import pandas as pd

filename = 'input'
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

positions_nda = np.array(positions)
velocities_nda = np.array(velocities)


def gen_dimensions_for_areas(iterations):
    areas = []
    for i in range(iterations):
        current_i_positions_nda = positions_nda + velocities_nda * i 
        x_min, y_min = current_i_positions_nda.min(axis=0)
        x_max, y_max = current_i_positions_nda.max(axis=0)
        w = x_max - x_min
        h = y_max - y_min
        a = w * h
        areas.append(a)
    return areas


def detect_inflection(areas):
    for i in range(len(areas) - 2):
        prev_area = areas[i]
        candidate_area = areas[i+1]
        next_area = areas[i+2]
        diff1 = candidate_area - prev_area
        diff2 = next_area - candidate_area
        if diff1 * diff2 < 0:
            return i+1


try_iterations = 11000  # after trying with: 10, 20, 100, 1000, 10000, 100000

dimensions_for_areas = gen_dimensions_for_areas(try_iterations)

iterations = detect_inflection(dimensions_for_areas)
print(f'Inflection i: {iterations}')  # 1027


def draw(positions_nda):

    x_min, y_min = positions_nda.min(axis=0)
    x_max, y_max = positions_nda.max(axis=0)
    
    for y in range(y_min, y_max + 1):
        line = ''
        for x in range(x_min, x_max + 1):
            if [x, y] in positions_nda.tolist():
                line += '#'
            else:
                line += '.'
        print(line)


positions_nda += velocities_nda * iterations

draw(positions_nda)

