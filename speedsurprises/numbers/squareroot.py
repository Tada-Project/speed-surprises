"""Compute the numerical square root function"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB


def square_root_exhaustive(value, epsilon):
    """Assumes value and epsilon are positive floats and epsilon < 1.
    Returns an answer such that answer*answer is within epsilon of value."""
    step = epsilon ** 2
    answer = 0.0
    while abs(answer ** 2 - value) >= epsilon and answer * answer <= value:
        answer += step
    if answer * answer > value:
        raise ValueError
    return answer


def square_root_bisection(value, epsilon):
    """Assumes value and epsilon are positive floats and epsilon < 1.
    Returns an answer such that answer*answer is within epsilon of value."""
    low = 0.0
    high = max(1.0, value)
    answer = (high + low) / 2.0
    while abs(answer ** 2 - value) >= epsilon:
        if answer ** 2 < value:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2.0
    return answer
