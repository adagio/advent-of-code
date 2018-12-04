from itertools import product

from modules.utils import Utils
from modules.frequencies import process as freq_process
from modules.checksum import process as check_process
from modules.checkrep import process as checkrep_process
from modules.commonchars import process as commonchars_process

# https://adventofcode.com/2018/day/2


def run():
    filepath = 'data/input.plain'
    ids = Utils.load_items(filepath)
    for id1, id2 in product(ids, ids):
        if id1 == id2:
            continue
        elif checkrep_process(id1, id2):
            print(f'id1: {id1}, id2: {id2}')
            cc = commonchars_process(id1, id2)
            print(cc)
            break


def run4():
    id1 = 'fghij'
    id2 = 'fguij'
    print(checkrep_process(id1, id2))


def run3():
    filepath = 'data/day02/input.plain'
    lines = Utils.load_items(filepath)
    freqs = []
    for line in lines:
        freq = freq_process(line)
        freqs.append(freq)
    result = check_process(freqs)
    print(result)


def run1():
    freqs = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 0]]
    print(check_process(freqs))


def run2():
    print(freq_process('bababc'))
