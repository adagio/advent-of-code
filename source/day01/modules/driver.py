from modules.utils import Utils
# from modules.addition import process as add_process
from modules.firsttwice import process

# https://adventofcode.com/2018/day/1


def run():
    filepath = 'data/input.plain'
    items = Utils.load_items(filepath)
    result = process(items)
    print(result)
