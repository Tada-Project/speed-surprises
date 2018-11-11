"""Tests for the bubble_sort function in the sorting module of the lists package"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from speedsurprises.lists import sorting


@pytest.mark.benchmark
def test_bubble_sort_benchmark(benchmark):
    """Benchmark the bubble_sort function"""
    sorted_list = benchmark(sorting.bubble_sort, list=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(
    test_list=lists(elements=integers(min_value=1, max_value=10), min_size=2),
)
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_bubble_sort_hypothesis_integer_lists_yes(test_list):
    """Sees if list of hypothesis-generated data sorted using bubble_sort is
    equal to same data sorted using Python's sort function"""
    bubble_sort_list = sorting.bubble_sort(test_list)
    # pylint: disable=W0622
    python_sort_list = test_list.sort()
    assert bubble_sort_list == python_sort_list


@pytest.mark.parametrize(
    "test_list, expected_answer",
    [([5, 3, 9, 2, 1]), ([1, 2, 3, 5, 9])],
)
def test_issubset_multiple(test_list, expected_answer):
    """Check the is_subset function with multiple inputs"""
    sorted_list = sorting.bubble_sort(test_list)
    assert sorted_list == expected_answer
