from collections import deque


def get_data(filename):

    filepath = f'data/{filename}.plain'

    data = None

    with open(filepath, 'r') as f:
        val_list = iter(int(x) for x in f.read().split())
        data = deque(val_list)

    return data

