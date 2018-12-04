from unittest import TestCase

from modules.reporter import Reporter


class ReporterTestCase(TestCase):

    def test_get_freqs_example_1(self):
        entries = [
            {'time': '00:05', 'ocurrence': 'falls'},
            {'time': '00:25', 'ocurrence': 'wakes'},
            {'time': '00:30', 'ocurrence': 'falls'},
            {'time': '00:55', 'ocurrence': 'wakes'}
        ]
        freqs = Reporter.get_freqs(entries)
        self.assertEqual(len(freqs), 45)

    def test_get_freqs_example_2(self):
        entries = [
            {'time': '00:40', 'ocurrence': 'falls'},
            {'time': '00:50', 'ocurrence': 'wakes'}
        ]
        freqs = Reporter.get_freqs(entries)
        self.assertEqual(len(freqs), 10)
