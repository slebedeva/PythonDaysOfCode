import unittest
from day15_leap_year import is_leap_year
class TestLeapYear(unittest.TestCase):

    def test_leap(self):
        assert is_leap_year(2000) == True
        assert is_leap_year(16) == True
        assert is_leap_year(1700) == False
