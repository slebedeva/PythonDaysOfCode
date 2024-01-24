import pytest

from day14_fibonacci import *
def test_print_fib(capfd):
    """
    To test function that prints a statement and returns None,
    we use pytest.capdf to capture stderr/stdout
    And use assert with the capture.
    Make sure to make capfd fixture the argument of the test function!
    """
    print_fibonacci(20)
    captured = capfd.readouterr()
    assert captured.out == "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]\n"
