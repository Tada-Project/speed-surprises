"""Test for max area problem."""

import pytest

from speedsurprises.leetcode import two_sum

lst = [2, 7, 11, 15]
target = 9
expected = [0, 1]


@pytest.mark.slow
def test_add_two_numbers_linear():
    """Test if two_sum_linear returns correct output."""
    output = two_sum.two_sum_linear(lst, target)
    assert output == expected


@pytest.mark.slow
def test_add_two_numbers_quadratic():
    """Test if two_sum_quadratic returns correct output."""
    output = two_sum.two_sum_quadratic(lst, target)
    assert output == expected
