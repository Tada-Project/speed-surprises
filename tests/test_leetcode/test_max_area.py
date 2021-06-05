"""Test for max area problem."""

from speedsurprises.leetcode import max_area

lst = [1, 8, 6, 2, 5, 4, 8, 3, 7]
expected = 49


def test_max_area_log():
    """Returns output with correct max area."""
    output = max_area.max_area_log(lst)
    assert output == expected


def test_max_area_linear():
    """Returns output with correct max area."""
    output = max_area.max_area_linear(lst)
    assert output == expected


def test_max_area_quadratic():
    """Returns output with correct max area."""
    output = max_area.max_area_quadratic(lst)
    assert output == expected
