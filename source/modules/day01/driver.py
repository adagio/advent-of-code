from modules.utils import Utils
#from modules.day01.addition import process as add_process
from modules.day01.firsttwice import process

# https://adventofcode.com/2018/day/1

def run():
    filepath = 'data/input.plain'
    items = Utils.load_items(filepath)
    result = process(items)
    print(result)
