"""Represent and/or manipulate sets"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(len(list_one) * len(list_two)) -- Quadratic
from functools import reduce


def is_subset(first_list, second_list):
    """Assumes first_list and second_list are lists.
    Returns True if each element in list_one is also
    in list_two and False otherwise."""
    for element_one in first_list:
        matched = False
        for element_two in second_list:
            if element_one == element_two:
                matched = True
                break
        if not matched:
            return False
    return True


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1
