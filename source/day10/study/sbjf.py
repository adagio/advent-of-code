import numpy as np
from scipy.optimize import minimize


def run(lines):

    x = []
    v = []

    for line in lines:
#        print(line[10:12])
#        print(line[14:16])
#        print(line[28:30])
#        print(line[32:34])
        x.append((int(line[10:12]), int(line[14:16])))
        v.append((int(line[28:30]), int(line[32:34])))
        #x.append((int(line[10:16]), int(line[18:24])))
        #v.append((int(line[36:38]), int(line[40:42])))
    
    x = np.array(x)
    v = np.array(v)

    def extent(t, positions, velocities):
        locs = positions + velocities*t
        return sum(np.max(locs, axis=0) - np.min(locs, axis=0))

    t = minimize(extent, 0, (x,v))
    print(f't: {t}')
    nit = t.nit
    print(f'nit: {nit}')
#    t = int(np.round(t.x))
