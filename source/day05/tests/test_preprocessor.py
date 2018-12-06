from unittest import TestCase

from modules.preprocessor import Preprocessor


class PreprocessorTestCase(TestCase):

    def setUp(self):
        self.polymer = 'dabAcCaCBAcCcaDA'

    def test_preprocess_example_1(self):
        preprocessed_polymer = Preprocessor().preprocess(self.polymer, 'A')
        self.assertEqual(preprocessed_polymer, 'dbcCCBcCcD')

    def test_preprocess_example_2(self):
        preprocessed_polymer = Preprocessor().preprocess(self.polymer, 'B')
        self.assertEqual(preprocessed_polymer, 'daAcCaCAcCcaDA')

    def test_preprocess_example_3(self):
        preprocessed_polymer = Preprocessor().preprocess(self.polymer, 'C')
        self.assertEqual(preprocessed_polymer, 'dabAaBAaDA')

    def test_preprocess_example_4(self):
        preprocessed_polymer = Preprocessor().preprocess(self.polymer, 'D')
        self.assertEqual(preprocessed_polymer, 'abAcCaCBAcCcaA')
