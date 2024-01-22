import unittest
from day11_multiplication_table import mult_table

class TestMultTable(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(mult_table(2), {1:2,2:4})
    def test_illegal(self):
        self.assertEqual(mult_table('0'), None)
