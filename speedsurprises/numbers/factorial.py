"""Compute the numerical factorial function."""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(n) -- Linear


def compute_iterative_factorial(value):
    """Assumes value is a natural number, returns value!."""
    if value < 0:
        raise ValueError("Inputs of 0 or greater!")
        value = 0
    result = 1
    while value != 0:
        result *= value
        value -= 1
    return result


def compute_recursive_factorial(value):
    """Compute the factorial function in a recursive fashion."""
    if value < 1:
        return 1
    else:
        return value * compute_recursive_factorial(value - 1)


def compute_hashmap_recursive_factorial(value):
    """Compute the factorial function in a recursive fashion with aid of hashmap/dictionary."""
    dictionary = {0: 1}
    if value not in dictionary:
        dictionary[value] = value * compute_hashmap_recursive_factorial(value - 1)
    return dictionary[value]
