""" Compute the recursive fibonacci function."""

# Inspiration and source for the function:
# Previous works.
# https://www.programiz.com/python-programming/examples/fibonacci-recursion

def compute_recursive_fibonacci(value):
    """ Assumes the value is a natural number. Returns the value!"""
    if(value <= 1):
        return value
    else:
        return compute_recursive_fibonacci(value - 2) + compute_recursive_fibonacci(value - 1)
