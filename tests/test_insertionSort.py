"""Tests for the bubble_sort function in the insertionSort module of the lists package"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from speedsurprises.lists import insertionSort


@pytest.mark.benchmark
def test_insertionSort_benchmark(benchmark):
    """Benchmark the insertionSort function"""
    sorted_list = benchmark(insertionSort.insertionSort, list=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_insertionSort_hypothesis(list):
    """Sees if list of hypothesis-generated data sorted is the same Python's sort function"""
    insertionSort_list = insertionSort.insertionSort(list)
    python_sort_list = sort.list()
    assert insertionSort_list == python_sort_list


@pytest.mark.parametrize(
    "list_input, expected_answer",
    [([6, 4, 8, 3, 2]), ([2, 3, 4, 6, 8])],
)

def test_insertionSort_multiple(list, expected_answer):
    """Check the insertionSort function with multiple lists"""
    sorted_list = insertionSort.insertionSort(list)
    assert sorted_list == expected_answer

def test_insertionSort_single():
    """Check the insertionSort function with a single list"""
    sorted_list = insertionSort.insertionSort([4, 3, 1, 5, 6])
    assert sorted_list == [1, 3, 4, 5, 6]
