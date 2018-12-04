# tasks on ./driver.md
import re
from collections import Counter

from modules.utils import Utils

from modules.preparer import Preparer
from modules.reporter import Reporter
from modules.reporter2 import Reporter2


def strategy2(filename):
    """
    Given the prepared and sorted csv file filename
    Returns the data to answer AOC
    """
    guard_times = Reporter2().produce_data2(filename)

    most = 0
    key = ()
    for guard, time in guard_times:
        value = guard_times[(guard, time)]
        # print(f'{k},{time}: {value}')
        if value > most:
            most = value
            key = (guard, time)

    print(most)
    print(key)
    guard, time = key
    product = guard * time
    print(f'product: {product}')


def report(filename):
    C, time_by_guards = Reporter2().produce_data(filename)
    # print(time_by_guards)
    worst_guard = Reporter2().report(C)
    # print(worst_guard)
    # times_by_worst_guard = time_by_guards[worst_guard]
    # print(times_by_worst_guard)
    freqs = Counter(time_by_guards[worst_guard])
    most_asleep_time, _ = freqs.most_common(1)[0]
    product = int(worst_guard) * most_asleep_time
    print(f'product: {product}')


def prepare(filename):

    in_filepath = f'data/{filename}.plain'

    prepared_filepath = in_filepath[:-6] + '.csv'
    Preparer().prepare_file(in_filepath, prepared_filepath)

    print('file prepared')

    sorted_filepath = in_filepath[:-6] + '-sorted.csv'
    Preparer().sort_file(prepared_filepath, sorted_filepath)

    print('lines sorted')


def run1():
    """
    minutes, guard #10
    """
    filepath = 'data/input-d-10.plain'
    lines = Utils.load_items(filepath)

    entries = []

    for line in lines:
        tokens = re.split(',', line)
        entry = {
            'date': tokens[0],
            'time': tokens[1],
            'ocurrence': tokens[2],
        }
        entries.append(entry)

    freqs = Reporter().get_freqs_by_date(entries)

    print(freqs)


def run2():
    """
    minutes, guard #10
    """
    filepath = 'data/input-m-99.plain'
    lines = Utils.load_items(filepath)

    entries = []

    for line in lines:
        tokens = re.split(',', line)
        entry = {
            'time': tokens[0],
            'ocurrence': tokens[1],
        }
        entries.append(entry)

    print(entries)

    freqs = Reporter.get_m_freqs(entries)

    print(freqs)
    print(len(freqs))
