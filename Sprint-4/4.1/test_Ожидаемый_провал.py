import pytest

@pytest.mark.xfail(reason="Known bug in calculation module, see TICKET-42")
def test_known_bug():
    # 0.1 + 0.2 в Python не равно в точности 0.3
    assert 0.1 + 0.2 == 0.3