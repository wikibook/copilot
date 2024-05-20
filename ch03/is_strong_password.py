def is_strong_password(password):
    """
    A strong password is not the word 'password'
    and is not the word 'qwerty'.

    Return True if the password is a strong password, False if not.
    """
    if password == "password" or password == "qwerty":
        return False
    else:
        return True


def is_strong_password(password):
    """
    A strong password has at least one uppercase character,
    at least one number, and at least one special symbol.

    Return True if the password is a strong password, False if not.
    """
    has_uppercase = False
    has_number = False
    has_special_symbol = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():
            has_special_symbol = True

    return has_uppercase and has_number and has_special_symbol


def is_strong_password(password):
    num_upper = 0
    num_num = 0
    num_special = 0

    for char in password:
        if char.isupper():
            num_upper += 1
        elif char.isnumeric():
            num_num += 1
        elif char in "!@#$%^&*":
            num_special += 1

    if num_upper >= 1 and num_num >= 1 and num_special >= 1:
        return True
    else:
        return False


def is_strong_password(password):
    """
    A strong password has at least one uppercase character,
        at least one number, and at least one punctuation.

    Return True if the password is a strong password, False if not.
    """
    has_uppercase = False
    has_number = False
    has_punctuation = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_number = True
        elif char in "!@#$%^&*":
            has_punctuation = True

    return has_uppercase and has_number and has_punctuation


import string


def is_strong_password(password):
    """
    A strong password has at least one uppercase character,
        at least one number, and at least one punctuation.

    Return True if the password is a strong password, False if not.
    """
    return (
        any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in string.punctuation for char in password)
    )
