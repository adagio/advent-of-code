# tasks on ./driver.md

import re
from collections import Counter

from modules.utils import Utils

from modules.reporter import Reporter

def run():
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

    freqs = Reporter.get_freqs(entries)

    print(freqs)
    print(len(freqs))
