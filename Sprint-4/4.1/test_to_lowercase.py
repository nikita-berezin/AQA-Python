from to_lowercase_text import to_lowercase


def test_text():
    assert to_lowercase("PyTest Is Awesome!") == "pytest is awesome!"
