from parse import parse
import numpy as np


def load_data(filename):

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

    return positions_nda, velocities_nda

