
def step(state, rules):
    """
    base on code by @fogleman at github
    https://github.com/fogleman/AdventOfCode2018/blob/master/12.py
    """
    most_left_idx = min(state)  # most left
    most_right_idx = max(state)
    range_start = most_left_idx - 2  # 2 to the left
    range_end = most_right_idx + 3  # 2 to the right
    # remember range() is not right inclusive

    # print(f'r_start: {range_start}, r_end: {range_end}')

    result = set()

    for i in range(range_start, range_end):
        # print(f'i: {i}')
        w = ''.join('#' if j in state else '.'
            for j in range(i-2, i+3))  # take the 5 boxes
        if w in rules and rules[w] == '#':
            result.add(i)
    return result

def trend_sum(initial_state, rules):
    """
    base on code by @emanuelfeld at observablehq
    https://beta.observablehq.com/@emanuelfeld/advent-of-code-2018-day-12
    """
    num_generations = 50_000_000_000;

    prev_sum = 0
    prev_diff = 0
    repeat_count = 0
    state = initial_state

    for g in range(num_generations):
        curr_sum = sum(state)

        if curr_sum - prev_sum == prev_diff:
            repeat_count += 1
        if repeat_count > 10:
            print(f'trend detected at iteration {g}')
            return curr_sum + (num_generations - g) * prev_diff
            # print(prev_sum + (curr_sum - prev_sum) * (50_000_000_000 - i))
            #  current sum + (        diff       ) * (      remaining    ) 
        else:
            prev_diff = curr_sum - prev_sum
            prev_sum = curr_sum
            state = step(state=state, rules=rules)

