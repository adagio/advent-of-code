from unittest import TestCase

from modules.frequencies import process


class FrequenciesTestCase(TestCase):

    def test_process_example_1(self):
        input_ = "abcdef"
        self.assertEqual(process(input_), [0, 0])

    def test_process_example_2(self):
        input_ = "bababc"
        self.assertEqual(process(input_), [1, 1])

    def test_process_example_3(self):
        input_ = "abbccd"
        self.assertEqual(process(input_), [1, 0])

    def test_process_example_4(self):
        input_ = "abcccd"
        self.assertEqual(process(input_), [0, 1])

    def test_process_example_5(self):
        input_ = "aabcdd"
        self.assertEqual(process(input_), [1, 0])

    def test_process_example_6(self):
        input_ = "abcdee"
        self.assertEqual(process(input_), [1, 0])

    def test_process_example_7(self):
        input_ = "ababab"
        self.assertEqual(process(input_), [0, 1])
