from unittest import TestCase

from modules.checksum import process


class ChecksumTestCase(TestCase):

    def test_process_example_1(self):
        input_ = [[0, 0], [1, 1], [1, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
        self.assertEqual(process(input_), 12)
