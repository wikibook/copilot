import random


def random_string(length):
    """
    length is an integer.

    Return a string of the given length, where each character
    is a digit from 0 to 9, and with no repeated digits.
    """
    s = ""
    while len(s) < length:
        r = random.randint(0, 9)
        if str(r) not in s:
            s += str(r)
    return s


def get_guess(length):
    """
    length is an integer.

    Keep asking the player to enter a string where each character
    is a digit from 0 to 9, until they enter a valid guess.
    A valid guess has the given length and has no repeated digits.
    """
    guess = input("Enter a guess: ")
    while len(guess) != length or not guess.isdigit() or len(set(guess)) != length:
        guess = input("Enter a guess: ")
    return guess


def guess_result(guess, secret_code):
    """
    guess and secret_code are strings of the same length.

    Return a list of two values:
    the first value is the number of indices in guess where
    the character at that index matches the character at the
    same index in secret_code; the second value is the
    number of indices in guess where the character at that
    index exists at a different index in secret_code.

    >>> guess_result('3821', '1862')
    [1, 2]
    >>> guess_result('1234', '4321')
    [0, 4]
    """
    correct = 0
    misplaced = 0
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            correct += 1
        elif guess[i] in secret_code:
            misplaced += 1
    return [correct, misplaced]


# import doctest

# doctest.testmod(verbose=True)


def play(num_digits, num_guesses):
    """
    Generate a random string with num_digits digits.
    The player has num_guesses guesses to guess the random
    string. After each guess, the player is told how many
    digits in the guess are in the correct place, and how
    many digits exist but are in the wrong place.
    """
    answer = random_string(num_digits)
    print("I generated a random {}-digit number.".format(num_digits))
    print("You have {} guesses to guess the number.".format(num_guesses))
    for i in range(num_guesses):
        guess = get_guess(num_digits)
        result = guess_result(guess, answer)
        print("Correct: {}, Misplaced: {}".format(result[0], result[1]))
        if guess == answer:
            print("You win!")
            return
    print("You lose! The correct answer was {}.".format(answer))
