def set_new_password(password):
    if len(password) < 8:
        raise ValueError("Пароль слишком короткий")
    return password

import pytest

def test_password_too_short_message():
    with pytest.raises(ValueError) as excinfo:
        set_new_password('1234567')
    assert "Пароль слишком короткий" in str(excinfo.value)