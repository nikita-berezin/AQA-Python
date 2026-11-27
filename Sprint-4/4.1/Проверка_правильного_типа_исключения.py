def get_user_by_id(user_id):

    if not isinstance(user_id, int):
        raise TypeError(f"{user_id} не является целым числом")

    existing_ids = [1, 2, 3, 100]
    if user_id not in existing_ids:
        raise ValueError(f"Пользователь с id {user_id} не найден")
    return user_id


import pytest


def test_user_not_found():

    with pytest.raises(TypeError) as excinfo:
        get_user_by_id("abc")
    assert "abc не является целым числом" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        get_user_by_id(999)
    assert "Пользователь с id 999 не найден" in str(excinfo.value)
