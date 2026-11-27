from find_errors import find_errors


def test_no_errors_found():
    assert not find_errors("корректные данные")
