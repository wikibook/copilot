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


# def get_strong_password():
#     """
#     Keep asking the user for a password until it is a strong
#     password, and return that strong password.
#     """
#     while True:
#         password = input("Enter a strong password: ")
#         if is_strong_password(password):
#             return password
#         else:
#             print("That password is not strong enough.")


def get_strong_password():
    """
    Keep asking the user for a password until it is a strong
    password, and return that strong password.
    """
    password = input("Enter a strong password: ")

    while not is_strong_password(password):
        password = input("Enter a strong password: ")
    return password
