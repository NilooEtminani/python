from initPy import is_acceptable_password
import pytest
@pytest.mark.parametrize("password, expected", [
    ("short", False),
    ("short54", True),
    ("muchlonger", True),
    ("ashort", False),
    ("muchlonger5", True),
    ("sh5", False),
    ("1234567", False),
    ("12345678910", True),
    ("password12345", False),
    ("PASSWORD12345", False),
    ("pass1234word", True)
])
def test_is_acceptable_password(password, expected):
    assert is_acceptable_password(password) == expected
pytest

