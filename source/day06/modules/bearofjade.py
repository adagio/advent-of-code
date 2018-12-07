def bear_run(filepath):

    coords = []
    infinite = {}
    areas = {(-1, -1): 0}

    with open(filepath) as f:
        while True:
            line = f.readline().strip('\n')
            if line != '':
                coords_tuple = line.split(', ')
                coord = (int(coords_tuple[0]), int(coords_tuple[1]))
                coords.append(coord)
                infinite[coord] = False
                areas[coord] = 0
            else:
                break

    print('Coords loaded')
    print(coords)
    print(len(coords))

    # grid = np.ones((10, 10))
    # print(grid)

    for i in range(500):
        for j in range(500):
            min_coord = (0, 0)
            min_dist = 1001
            for coord in coords:  # for every coord
                dist = abs(coord[0] - i) + abs(coord[1] - j)

                if dist < min_dist:  # search min_dist
                    min_dist = dist  # update min_dist
                    min_coord = coord  # update min_coord
                elif dist == min_dist:
                    min_coord = (-1, -1)  # hypotetic comodin coor

            if i == 499 or i == 0 or j == 499 or j == 0:  # for first or last execution of double loop
                #  at the begining and at the end
                #  a initial value and update
                infinite[min_coord] = True

            areas[min_coord] += 1  # accumulate area for min_coord, for this double loop

    maxA = 0
    for key, value in areas.items():
        if value > maxA and not infinite[key]:
            maxA = value

    print(maxA)
