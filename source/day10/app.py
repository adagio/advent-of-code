import numpy as np

from modules.observador import gen_areas
from modules.observador import detect_inflection

from modules.dibujante import draw

from modules.utils import load_data


filename = 'input'

positions_nda, velocities_nda = load_data(filename)

# identify the second that minimizes the dispersion of points
# it's sufficient to detect work with just one of the axis
# let's work with the dispersion along y axis

try_iterations = 11000  # after trying with: 10, 20, 100, 1000, 10000, 100000

areas = gen_areas(try_iterations, positions_nda,
        velocities_nda)

iterations = detect_inflection(areas)
print(f'Inflection i: {iterations}')  # 1027

positions_nda += velocities_nda * iterations

draw(positions_nda)

