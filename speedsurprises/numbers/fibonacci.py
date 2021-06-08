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


def fibonacci_tuple(n):
    """Compute fibonacci and return in a tuple container."""
    result = ()
    a = 1
    b = 1
    for i in range(n):
        result += (a,)
        a, b = b, a + b
    return result


def fibonacci_list(n):
    """Compute fibonacci and return in a list container."""
    result = []
    a = 1
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_generator(n):
    """Compute fibonacci through generator and return for testing purpose."""
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
    return a
