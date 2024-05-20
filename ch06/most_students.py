def most_students(classroom):
    """
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student
    How many new students can sit in a row?
    """
    max_students = 0
    for row in classroom:
        students = 0
        for seat in row:
            if seat == "S":
                students += 1
            else:
                students = 0
            if students > max_students:
                max_students = students
    return max_students


def most_students(classroom):
    """
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student
 
    How many new students can sit in a row?
 
    >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], \
                        [' ', 'S', 'S', 'S', 'S', 'S'], \
                        [' ', 'S', ' ', 'S', ' ', ' ']]) 
    4
    """
    max_students = 0
    for row in classroom:
        students = 0
        for seat in row:
            if seat == "S":
                students += 1
            else:
                students = 0
            if students > max_students:
                max_students = students
    return max_students


import doctest

doctest.testmod(verbose=False)


def most_students(classroom):
    """
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student
 
    Return the maximum total number of ' ' characters in a
    given row. 
 
    >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], \
                            [' ', 'S', 'S', 'S', 'S', 'S'], \
                            [' ', 'S', ' ', 'S', ' ', ' ']])
    4
    """
    max_seats = 0
    for row in classroom:
        seats = row.count(" ")
        if seats > max_seats:
            max_seats = seats
    return max_seats


import doctest

doctest.testmod(verbose=False)


def most_students(classroom):
    """
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student
 
    Return the maximum total number of ' ' characters in a 
    given row. 

    >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], \
                        [' ', 'S', 'S', 'S', 'S', 'S'], \
                        [' ', 'S', ' ', 'S', ' ', ' ']])
    4
    >>> most_students([['S', 'S', 'S'], \
                        ['S', 'S', 'S'], \
                        ['S', 'S', 'S']])
    0
    >>> most_students([['S', 'S', 'S'], \
                        [' ', ' ', ' '], \
                        ['S', 'S', 'S']])
    3
    >>> most_students([[' ', ' ', 'S'], \
                        ['S', ' ', ' '], \
                        ['S', 'S', 'S']])
    2
    """
    max_seats = 0
    for row in classroom:
        seats = row.count(" ")
        if seats > max_seats:
            max_seats = seats
    return max_seats


import doctest

doctest.testmod(verbose=False)
