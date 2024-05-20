# write a function that returns the larger of two numbers
# input is two numbers
# output is the larger of the two numbers


def larger_of_two_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def larger(num1, num2):
    """
    num1 and num2 are two numbers.
    Return the larger of the two numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2


# call the larger function with the values 3 and 5
# store the result in a variable called result
# then print result
result = larger(3, 5)
print(result)
