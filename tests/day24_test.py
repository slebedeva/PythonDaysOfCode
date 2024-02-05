import pytest
from day24_remove_vowels import remove_vowels

def test_day24():
    assert remove_vowels('Au') == ''
    # check that it raises typeerror if input is not a string
    with pytest.raises(TypeError):
        remove_vowels(567)
