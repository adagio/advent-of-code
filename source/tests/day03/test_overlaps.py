from unittest import TestCase

from modules.day03.overlaps import how_many_overlaps
from modules.day03.overlaps import get_non_overlapped_coords

class OverlapsTestCase(TestCase):

    def test_overlaps(self):
        lines = [
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2'
        ]
        self.assertEqual(how_many_overlaps(lines), 4)

    def test_non_overlapped(self):
        lines = [
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2'
        ]
        self.assertEqual(len(get_non_overlapped_coords(lines)), 28)
