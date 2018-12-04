from unittest import TestCase

from modules.checkrep import process


class CheckRepTestCase(TestCase):

    def test_process_example_1(self):
        id1 = 'fghij'
        id2 = 'fguij'
        self.assertEqual(process(id1, id2), True)

    def test_process_example_2(self):
        id1 = 'fghit'
        id2 = 'fguij'
        self.assertEqual(process(id1, id2), False)
