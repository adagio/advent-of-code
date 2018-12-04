from unittest import TestCase

from modules.parse import parse


class ParseTestCase(TestCase):

    def test_parse_example_1(self):
        text = "#1 @ 3,2: 5x4"
        claim_obj = {
            "id": 1,
            "left_edge": 3,
            "top_edge": 2,
            "width": 5,
            "height": 4
        }
        self.assertEqual(parse(text), claim_obj)
