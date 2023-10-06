def is_acceptable_password(password: str) -> bool:
    if (len(password) > 6 and any(char.isdigit() for char in password) and password.isdigit() == False):
        return True
    elif len(password) > 9:
        return True
    else:
        return False


