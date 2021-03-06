#
#  https://www.reddit.com/r/adventofcode/comments/a3kr4r/2018_day_6_solutions/eb7a0zn/

from io import StringIO
import numpy as np


test_data = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""


def part_ab(data, d_max=10000):
    vs = np.loadtxt(StringIO(data), dtype=int, delimiter=',')
    w, h = vs.max(axis=0) + 1
    n = len(vs)
    py, px = np.mgrid[:w, :h]
    ps = np.c_[py.ravel(), px.ravel()]
    ds = np.abs(ps[:, None] - vs).sum(axis=2)
    d = ds.argmin(axis=1)
    ties = d != n - 1 - np.fliplr(ds).argmin(axis=1)
    d[ties] = -1
    border = {*d[:w], *d[-w:], *d[::h], *d[::-h]}
    areas = [(d == c).sum() for c in range(n) if c not in border]
    part_a = max(areas)
    part_b = (ds.sum(axis=1) < d_max).sum()
    return part_a, part_b


a, b = part_ab(test_data, d_max=32)  # == (17, 16)
# a, b = part_ab(data)
print(a)  # 3293
print(b)  # 45176
