import functools


def is_armstrong_number(number):
    digits = [pow(int(digit), len(str(number))) for digit in str(number)]
    return number == functools.reduce(lambda a, b: a+b, digits)
