""" Compute the fibonacci function."""

# Inspiration and source for the function:
# Previous works.
# https://www.programiz.com/python-programming/examples/fibonacci-recursion  (for recursive)


def compute_recursive_fibonacci(value):
    """ Assumes the value is a natural number. Returns the value!"""
    if value <= 1:
        return value
    else:
        return compute_recursive_fibonacci(value - 2) + compute_recursive_fibonacci(
            value - 1
        )


def compute_iterative_fibonacci(value):
    """Compute fibonacci iteratively"""
    if value <= 1:
        return value
    else:
        x = 0
        y = 1
        for i in range(1, value):
            z = x + y
            x = y
            y = z
        return y


def fibonacci_tuple(n):
    """Fibonacci with tuple container."""
    result = ()
    a = 1
    b = 1
    for i in range(n):
        result += (a,)
        a, b = b, a + b
    return result


def fibonacci_list(n):
    """Fibonacci with list container."""
    result = []
    a = 1
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_generator(n):
    """Fibonacci generator with no container."""
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
    return a
