import pytest
from day12_invert_str import invert_str

def test_d12():
    assert invert_str('foo') == 'oof'
    assert invert_str(0) == None
