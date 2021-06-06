"""Compute the output of the fibonacci function."""

# Inspiration and source for the function:
# Previous works.
# https://www.programiz.com/python-programming/examples/fibonacci-recursion  (for recursive)


def compute_recursive_fibonacci(value):
    """Compute fibonacci number in recursive fashion, assumes the value is a natural number."""
    if value <= 1:
        return value
    return compute_recursive_fibonacci(value - 2) + compute_recursive_fibonacci(
        value - 1
    )


def compute_iterative_fibonacci(value):
    """Compute the fibonacci number in an iterative fashion."""
    if value <= 1:
        return value
    x = 0
    y = 1
    # pylint: disable=unused-variable
    for i in range(1, value):
        z = x + y
        x = y
        y = z
    return y
