# Write a simple unit test for a function that adds two numbers

import unittest
from day35_unittest import add_two


class TestAddTwo(unittest.TestCase):
    def test_add(self):
        # code from Lawrence
        try:
            self.assertEqual(add_two(8,9),17)
        except AssertionError:
            print('Summing test failed')
    def test_err(self):
        try:
            with self.assertRaises(TypeError):
                add_two('foo',2)
        except AssertionError:
            print('Type error test failed')
            
# thanks to Lawrence: test with printed output            
if __name__ == '__main__': # this is needed to run the test below
    print("Testing add using 'unittest' module...")
    unittest.main() # this will run the test above
    print("Done with testing using 'unittest' module...")
    print()
