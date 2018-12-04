from unittest import TestCase

from modules.firsttwice import process


class FirstTwiceTestCase(TestCase):

    def test_process_example_1(self):
        input_ = "+1, -1".split(', ')
        self.assertEqual(process(input_), 0)

    def test_process_example_2(self):
        input_ = "+3, +3, +4, -2, -4".split(', ')
        self.assertEqual(process(input_), 10)

    def test_process_example_3(self):
        input_ = "-6, +3, +8, +5, -6".split(', ')
        self.assertEqual(process(input_), 5)

    def test_process_example_4(self):
        input_ = "+7, +7, -2, -7, -4".split(', ')
        self.assertEqual(process(input_), 14)
