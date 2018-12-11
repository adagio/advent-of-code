import numpy as np
from scipy.optimize import minimize

from modules.observador import gen_area
from modules.dibujante import draw
from modules.utils import load_data


filename = 'input'

positions_nda, velocities_nda = load_data(filename)

# identify the second that minimizes the dispersion of points
t = minimize(gen_area, 0, (positions_nda, velocities_nda))
second = int(np.round(t.x))

positions_nda += velocities_nda * second

draw(positions_nda)

