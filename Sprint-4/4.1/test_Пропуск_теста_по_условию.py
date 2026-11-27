import sys

import pytest

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
def test_python310_feature():
    value = 1

    match value:
        case 1:
            assert True