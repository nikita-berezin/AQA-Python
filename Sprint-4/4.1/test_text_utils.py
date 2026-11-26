from text_utils import is_palindrome

def test_1():
    assert is_palindrome('топот') is True

def test_2():
    assert is_palindrome('Топот') is True

def test_3():
    assert is_palindrome('python') is False

def test_4():
    assert is_palindrome('А') is True