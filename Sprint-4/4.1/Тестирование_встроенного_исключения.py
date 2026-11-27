import pytest

def test_pop_from_empty_list():
    empty_list = []
    with pytest.raises(IndexError):
        empty_list.pop()