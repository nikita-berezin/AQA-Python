from get_supported_formats import get_supported_formats


def test_supports_jpeg():
    assert "jpeg" in get_supported_formats()
