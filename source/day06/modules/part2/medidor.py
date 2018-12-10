import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed


def __get_grid(coords):
    x_min, y_min = coords.min(axis=0)  # - 1
    x_max, y_max = coords.max(axis=0)  # + 2

    py, px = np.mgrid[x_min:x_max, y_min:y_max]

    px_ravel = px.ravel()
    py_ravel = py.ravel()

    grid = np.c_[py_ravel, px_ravel]

    return grid


def __get_distance_sum(point, coords, cota):
    distance_sum = 0
    p_x, p_y = point
    for coord in coords:
        coord_x, coord_y = coord
        distance_to_coord = abs(p_x - coord_x) + abs(p_y - coord_y)
        distance_sum += distance_to_coord
        if distance_sum > cota:
            break
    return distance_sum


def __get_largest_area_by_grid(grid, coords, cota):
    area = []

    for point in grid:
        distance_sum = __get_distance_sum(point, coords, cota)
        if distance_sum < cota:
            area.append(distance_sum)

    return area


def __get_largest_area_by_row(grid, row_index, x_max, coords, cota):
    # print(f'row_index: {row_index}')
    start = x_max*(row_index - 1)
    end = x_max*row_index
    row = grid[start:end]
    row_area = __get_largest_area_by_grid(row, coords, cota)
    return row_area


def get_largest_area(coords, cota):

    grid = __get_grid(coords)

    # area = __get_largest_area_by_grid(grid, coords, cota)
    x_min, y_min = coords.min(axis=0)  # - 1
    x_max, y_max = coords.max(axis=0)  # + 2

    area = []

    y_range = range(y_min, y_max - 1)

    with ProcessPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(__get_largest_area_by_row, grid, row_index, x_max, coords, cota) for row_index in y_range]
        for completed_futures in as_completed(futures):
            row_area = completed_futures.result()
            area.extend(row_area)

    return area

