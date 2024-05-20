# def most_students(classroom):
#     """
#     classroom is a list of lists
#     Each ' ' is an empty seat
#     Each 'S' is a student
#     Find the most students seated consecutively in a row
#     >>> most_students([['S', ' ', 'S', ' ', 'S', 'S'], \
#                             ['S', ' ', 'S', 'S', 'S', ' '], \
#                             [' ', 'S', ' ', 'S', ' ', ' ']])
#     3
#     >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], \
#                        ['S', ' ', 'S', 'S', 'S', ' '], \
#                        [' ', 'S', ' ', 'S', ' ', ' ']])
#     4
#     """
#     max_count = 0
#     for row in classroom:
#         count = 0
#         for seat in row:
#             if seat == "S":
#                 count += 1
#             else:
#                 if count > max_count:
#                     max_count = count
#                 count = 0
#     return max_count


# import doctest

# doctest.testmod(verbose=True)


def most_students(classroom):
    """
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student

    Find the most students seated consecutively in a row
    >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], \
                            ['S', ' ', 'S', 'S', 'S', ' '], \
                            [' ', 'S', ' ', 'S', ' ', ' ']]) 
    4
    """
    max_count = 0
    for row in classroom:
        count = 0
        for seat in row:
            if seat == "S":
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
    return max_count


import doctest

doctest.testmod(verbose=True)
