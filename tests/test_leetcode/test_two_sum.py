"""Test for two sum problem."""

from speedsurprises.leetcode import two_sum

lst = [2, 7, 11, 15]
target = 9
expected = [0, 1]


def test_two_sum_linear():
    """Test if two sum linear returns correct output."""
    output = two_sum.two_sum_linear(lst, target)
    assert output == expected


def test_two_sum_linear_no_match():
    """Test if two sum linear returns empty list when there is no match."""
    output = two_sum.two_sum_linear(lst, 5)
    assert output == []


def test_two_sum_quadratic():
    """Test if two sum quadratic returns correct output."""
    output = two_sum.two_sum_quadratic(lst, target)
    assert output == expected


def test_two_sum_quadratic_no_match():
    """Test if two sum quadratic returns empty list when there is no match."""
    output = two_sum.two_sum_quadratic(lst, 5)
    assert output == []
