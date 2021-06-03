"""Test for subsets problem."""

from speedsurprises.leetcode import subsets


def test_subsets_backtrack():
    """Test subset backtrack returns the correct output."""
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    output = subsets.subsets_backtrack(nums)
    assert output == expected


def test_subsets_backtrack_iterative():
    """Test subset iterative returns the correct output."""
    nums = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    output = subsets.subsets_iterative(nums)
    assert output == expected
