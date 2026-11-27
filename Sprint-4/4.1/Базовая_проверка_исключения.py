def divide(a, b):
    if b == 0:
        raise ValueError('На 0 делить нельзя')
    return a / b

import pytest

def test_division_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert 'На 0 делить нельзя' in str(excinfo.value)