from initPy import is_acceptable_password
import unittest
def test_is_acceptable_password_short():
    assert is_acceptable_password("short") == False

def test_is_acceptable_password_short54():
    assert is_acceptable_password("short54") == True

def test_is_acceptable_password_muchlonger():
    assert is_acceptable_password("muchlonger") == True

def test_is_acceptable_password_ashort():
    assert is_acceptable_password("ashort") == False

def test_is_acceptable_password_muchlonger5():
    assert is_acceptable_password("muchlonger5") == True

def test_is_acceptable_password_sh5():
    assert is_acceptable_password("sh5") == False

def test_is_acceptable_password_1234567():
    assert is_acceptable_password("1234567") == False

def test_is_acceptable_password_12345678910():
    assert is_acceptable_password("12345678910") == True

def test_is_acceptable_password_password12345():
    assert is_acceptable_password("password12345") == False

def test_is_acceptable_password_PASSWORD12345():
    assert is_acceptable_password("PASSWORD12345") == False

def test_is_acceptable_password_pass1234word():
    assert is_acceptable_password("pass1234word") == True