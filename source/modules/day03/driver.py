from modules.utils import Utils
from modules.day03.claim import DataClassClaim
from modules.day03.overlaps import how_many_overlaps
from modules.day03.overlaps import get_non_overlapped_coords
from modules.day03.overlaps import get_non_overlapped_claim

# https://adventofcode.com/2018/day/3

def run():
    """
    Part 2
    """
    filepath = 'data/day03/input.plain'
    lines = Utils.load_items(filepath)
    #non_overlapped_coords = get_non_overlapped_coords(lines)
    non_overlapped_claim = get_non_overlapped_claim(lines)
    print(non_overlapped_claim.id)

def run1():
    """
    Part 1
    """
    filepath = 'data/day03/input.plain'
    lines = Utils.load_items(filepath)
    total = how_many_overlaps(lines)
    print(total)

def run1():
    obj = {
        "id": 1,
        "left_edge": 3,
        "top_edge": 2,
        "width": 5,
        "height": 4
    }
    claim = DataClassClaim(**obj)
    print(claim)
