# Day 06

## Best for part 06

### om_henners

with numpy

### wimglenn

with numpy

### pythondevbg

functionality decomposed in functions

### marcus

from 0 to x_max ...

### bearofjade

my analysis started with his code
i added inlnie comments to his code

### protectedmethod

could be usefu

    area = []

    with ProcessPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(__get_distance_sum, point, coords, cota) for point in grid]
        for completed_futures in as_completed(futures):
            distance_sum = completed_futures.result()
            if distance_sum < cota:
                print(distance_sum)
                area.append(distance_sum)
