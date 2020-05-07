"""Test for max area problem"""

from speedsurprises.leetcode import two_sum

lst = [2, 7, 11, 15]
target = 9
expected = [0, 1]


def test_add_two_numbers_linear():
    """test if returns correct output"""
    output = two_sum.two_sum_linear(lst, target)
    assert output == expected


def test_add_two_numbers_quadratic():
    """test if returns correct output"""
    output = two_sum.two_sum_quadratic(lst, target)
    assert output == expected
