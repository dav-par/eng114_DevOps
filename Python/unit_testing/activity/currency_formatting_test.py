from currency_formatting import Money
import unittest

class Moneytests(unittest.TestCase):

    money = Money(500)

    def test_add(self):
        self.assertEqual(self.money.add(2, 4), 6)

    def test___format__(self):
        self.assertIn(self.money.__format__("dollars"), "$625.00")

'''
    def test___format__(self):
        self.assertTrue(self.money.__format__("dollars"),
'''