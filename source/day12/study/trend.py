from collections import defaultdict
from modules.evolution import step


def plot_trend(state, rules):
    """
    base on code by @emanuelfeld at observablehq
    https://beta.observablehq.com/@emanuelfeld/advent-of-code-2018-day-12
    """
    sums = defaultdict(int)
    curr_sum = prev_sum = 0

    for i in range(200):
        prev_sum = curr_sum
        state = step(state, rules)
        curr_sum = sum(state)
        sums[i] = curr_sum

    import matplotlib as mpl
    mpl.use('TkAgg')
    import matplotlib.pylab as plt

    x = sums.keys()
    y = sums.values()
    plt.plot(x, y)
    plt.show()

