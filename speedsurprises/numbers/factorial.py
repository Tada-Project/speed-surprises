"""Compute the numerical factorial function"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(n) -- Linear


def compute_iterative_factorial(value):
    """Assumes value is a natural number
    Returns value!"""
    if value < 0:
        ValueError("Inputs of 0 or grater!")
        value = 0
    result = 1
    while value != 0:
        result *= value
        value -= 1
    return result


def compute_recursive_factorial(value):
    if value < 1:
        return 1
    else:
        return value * compute_recursive_factorial(value - 1)


def compute_hashmap_recursive_factorial(value):
    dict = {0: 1}
    if value not in dict:
        dict[value] = value * compute_hashmap_recursive_factorial(value - 1)
    return dict[value]
