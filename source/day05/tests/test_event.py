from unittest import TestCase

from modules.event import Event


class EventTestCase(TestCase):

    def test_trigger_units_of_example_1(self):
        polymer = 'dabAcCaCBAcCcaDA'
        result = Event().trigger_units_of(polymer)
        self.assertEqual(result, 'dabCBAcaDA')
