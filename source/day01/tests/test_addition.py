from unittest import TestCase

from modules.addition import process


class AdditionTestCase(TestCase):

    def test_process_example_1(self):
        input_ = "+1, +1, +1".split(', ')
        self.assertEqual(process(input_), 3)

    def test_process_example_2(self):
        input_ = "+1, +1, -2".split(', ')
        self.assertEqual(process(input_), 0)

    def test_process_example_3(self):
        input_ = "-1, -2, -3".split(', ')
        self.assertEqual(process(input_), -6)
