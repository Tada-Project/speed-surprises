"""Compute the numerical factorial function"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(n) -- Linear


def compute_factorial(value):
    """Assumes value is a natural number
    Returns value!"""
    answer = 1
    while value > 1:
        answer *= value
        value = value - 1
    return answer

def recursive_fibonacci(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return recursive_fibonacci(value-1) + recursive_fibonacci(value-2)

def iterative_fibonacci(value):
    if (value == 0):
        return 0
    else:
        x = 0
        y = 1
        for i in range(1, value):
            z = (x + y)
            x = y
            y = z
        return y
