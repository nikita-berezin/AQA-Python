def get_user_info(dict1):
    return dict1


dict1 = {
    "id": 101,
    "name": "Alice",
    "status": "active",
}


def test_user_data():
    assert get_user_info(dict1) == {
        "id": 101,
        "name": "Alice",
        "status": "active",
    }
