"""Test for maximum subarray problem."""

from speedsurprises.leetcode import maximum_subarray

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6


def test_brute_force_with_long_list():
    """Test the brute force appraoch returns correct result."""
    output = maximum_subarray.brute_force(nums)
    assert output == expected


def test_two_pointers_with_long_list():
    """Test the two pointers appraoch returns correct result."""
    output = maximum_subarray.two_pointers(nums)
    assert output == expected


def test_kadane_with_long_list():
    """Test the dynamic programming kadane appraoch returns correct result."""
    output = maximum_subarray.kadane(nums)
    assert output == expected


def test_optimized_kadane_with_long_list():
    """Test the optimized kadane appraoch returns correct result."""
    output = maximum_subarray.optimized_kadane(nums)
    assert output == expected


def test_divide_and_conquer_with_long_list():
    """Test the divide and conquer appraoch returns correct result."""
    output = maximum_subarray.divide_and_conquer(nums)
    assert output == expected


def test_brute_force_with_one_element_list():
    """Test the brute force appraoch returns correct result."""
    output = maximum_subarray.brute_force([1])
    assert output == 1


def test_two_pointers_with_one_element_list():
    """Test the two pointers appraoch returns correct result."""
    output = maximum_subarray.two_pointers([1])
    assert output == 1


def test_kadane_with_one_element_list():
    """Test the dynamic programming kadane appraoch returns correct result."""
    output = maximum_subarray.kadane([1])
    assert output == 1


def test_kadane_with_empty_list():
    """Test the dynamic programming kadane appraoch returns correct result."""
    output = maximum_subarray.kadane([])
    assert output == 0


def test_optimized_kadane_with_one_element_list():
    """Test the optimized kadane appraoch returns correct result."""
    output = maximum_subarray.optimized_kadane([1])
    assert output == 1


def test_divide_and_conquer_with_one_element_list():
    """Test the divide and conquer appraoch returns correct result."""
    output = maximum_subarray.divide_and_conquer([1])
    assert output == 1
