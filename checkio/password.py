"""
Module for password validation.
"""

def is_acceptable_password(password: str) -> bool:
    """
    Check if a password is acceptable based on length and content.

    Args:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is acceptable, False otherwise.
    """
    if len(password) > 6 and any(char.isdigit() for char in password) and not password.isdigit():
        return True
    return len(password) > 9
