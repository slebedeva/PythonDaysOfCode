import pytest
from day10_remove_dup import remove_duplicates

def test_day10():
    assert remove_duplicates([9,4,4,8,7,6,9]) == [9,4,8,7,6]
