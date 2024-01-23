import unittest
from day13_shuffle_list import shuffle_list

class testShuffle(unittest.TestCase):
    def test_shuffle(self):
        self.assertEqual([7, 3, 2, 8, 5, 6, 9, 4, 0, 1],
                         shuffle_list(list(range(10))))
