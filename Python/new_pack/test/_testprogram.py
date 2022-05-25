from ..app import fizzbuzz
import unittest

class Calctests(unittest.fizzbuzz):

    fizz = fizzbuzz()

    def test_add(self):
        self.assertEqual(self.fizz.add(2, 4), 6)
