"""Compute the basic multiplication and division function."""


def compute_multiplication(value):
    """Perform multiplication."""
    answer = value * value
    return answer


def compute_division(value):
    """Perform division."""
    # WARNING: this uses "old division" and may not work in the future
    # pylint: disable=old-division
    answer = value / value
    return answer
