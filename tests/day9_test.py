import unittest
from day9_even_odd import even_odd

class TestEvenOdd(unittest.TestCase):
    def test_odd_even(self):
        # test an even number
        assert even_odd(8) == 'even'
        assert even_odd(9) == 'odd'
        assert even_odd('foo') == None
