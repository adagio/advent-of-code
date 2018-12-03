from unittest import TestCase

from modules.day02.commonchars import process

class CommonCharsTestCase(TestCase):

    def test_process_example_1(self):
        id1 = 'fghij'
        id2 = 'fguij'
        self.assertEqual(process(id1, id2), 'fgij')

    def test_process_example_2(self):
        id1 = 'fghit'
        id2 = 'fghij'
        self.assertEqual(process(id1, id2), 'fghi')