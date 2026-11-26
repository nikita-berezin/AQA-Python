from numbers_utils import is_even


def test_even_four():
    assert is_even(4) is True

def test_odd_seven():
    assert is_even(7) is False

def test_even_zero():
    assert is_even(0) is True

def test_even_two():
    assert is_even(2) is True