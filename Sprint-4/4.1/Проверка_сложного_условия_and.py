def get_score(num):
    return num

def test_score_is_in_valid_range():
    assert get_score(60) > 50 and get_score(60) < 100