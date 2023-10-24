from checkio import password
import pytest


def test_is_acceptable_password():
    # Test cases where the password should be considered acceptable
    assert password.is_acceptable_password("short54") == True
    assert password.is_acceptable_password("muchlonger5") == True
    assert password.is_acceptable_password("muchlonger123") == True

    # Test cases where the password should be considered unacceptable
    assert password.is_acceptable_password("short") == False
    assert password.is_acceptable_password("ashort") == False
    assert password.is_acceptable_password("sh5") == False

    # Test case with a numeric password
    assert password.is_acceptable_password("1234567") == False

    # Test case with a password shorter than 6 characters
    assert password.is_acceptable_password("pass") == False

    # Test case with a password longer than 6 characters but no digits
    assert password.is_acceptable_password("nopass") == False

    # Test case with a password longer than 9 characters but no digits
    assert password.is_acceptable_password("nopassword") == True

    # Test case with a password longer than 9 characters and contains digits
    assert password.is_acceptable_password("password123") == True

    # Test case with an empty password
    assert password.is_acceptable_password("") == False

    # Test case with a password consisting of digits only
    assert password.is_acceptable_password("1234567890") == True
