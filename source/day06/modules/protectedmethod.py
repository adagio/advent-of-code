def method(filepath):

    with open(filepath, 'r') as f:
        lines = map(lambda x: x.strip(), f.readlines());

    points = set();

    for line in lines:
        points.add(tuple([int(j.strip()) for j in line.split(",")]));

    areas = {};

    min_x = min(points, key=lambda x: x[0])[0];
    max_x = max(points, key=lambda x: x[0])[0];
    min_y = min(points, key=lambda x: x[1])[1];
    max_y = max(points, key=lambda x: x[1])[1];

    print(min_x, min_y, max_x, max_y);

    def find_closest_point(x, y):
        distances = {};
        for point in points:
            distances[point] = abs(point[1] - y) + abs(point[0] - x);

        minimum = min(distances.items(), key=lambda x: x[1]);
        min_distance = minimum[1];
        count = 0;
        for k, v in distances.items():
            if(v == min_distance):
                count += 1;

        return minimum[0] if count == 1 else None;



    infinite_points = set();

    sizes = {};

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            closest = find_closest_point(x, y);
            if(closest):
                if(x in (0, max_x, ) or y in (0, max_y, )):
                    infinite_points.add(closest);
                    if(closest in sizes):
                        del sizes[closest];
                    continue;
                if(not closest in sizes):
                    sizes[closest] = 1;
                else:
                    sizes[closest] += 1;


    print(sizes);

    maximum = max(sizes.items(), key=lambda x: x[1] if x[0] not in infinite_points else -1);

    print(maximum);
