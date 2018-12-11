def gen_areas(iterations, positions_nda, velocities_nda):
    """
    Given iterations, positions and velocities
    Return areas. Areas are dimensions (w*h)
    """
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

