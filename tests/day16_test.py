import pytest
from day16_token_counter import count_tokens
def test_counter():
    assert count_tokens('I like cookies!!!') == {'i': 1, 'like': 1, 'cookies': 1}
