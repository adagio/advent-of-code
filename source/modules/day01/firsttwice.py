from itertools import cycle
from collections import Counter

def process(items):
    """
    Given a array of strings ["+1", "-2"]
    calculate the frequency reached twice
    """
    times = True
    sum = 0
    iteritems = cycle(items)
    freqs = Counter()
    freqs[0] += 1

    for item in iteritems:
        sum = sum + int(item)
        #print(f'sum: {sum}')
        freqs[sum] += 1
        #print(f'freqs[{sum}]: {freqs[sum]}')
        if freqs[sum]==2:
            break

    return sum