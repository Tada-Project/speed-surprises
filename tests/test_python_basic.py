"""Tests for python_basic functions in the python_basic module of the lists package."""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from speedsurprises.lists import python_basic


def test_list_delete_index():
    """Check the removal of a value from the list."""
    list_input = [2, 4, 6, 8, 10]
    list_input_copy = list_input.copy()
    removed_value_list = python_basic.list_delete_item_random(list_input)
    assert len(removed_value_list) == len(list_input_copy) - 1


def test_list_delete_index_empty_list():
    """Check the removal of a value from the empty list."""
    list_input = []
    list_input_copy = list_input.copy()
    removed_value_list = python_basic.list_delete_item_random(list_input)
    assert len(removed_value_list) == len(list_input_copy)


@pytest.mark.benchmark
def test_list_copy_benchmark(benchmark):
    """Benchmark the list_copy function."""
    copied_list = benchmark(python_basic.list_copy, thelist=[1, 2, 3, 4])
    assert copied_list == [1, 2, 3, 4]


@given(listInput=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_list_copy_hypothesis(listInput):
    """Using hypothesis."""
    copied_list = python_basic.list_copy(listInput)
    assert copied_list == listInput


@pytest.mark.parametrize(
    "list_input, expected_answer",
    [([2, 3, 4, 6, 8], [2, 3, 4, 6, 8]), ([1, 2, 3, 4], [1, 2, 3, 4])],
)
def test_list_copy_multiple(list_input, expected_answer):
    """Check the list_copy function with multiple lists."""
    copied_list = python_basic.list_copy(list_input)
    assert copied_list == expected_answer


def test_list_copy_single():
    """Check the list_copy function with a single list."""
    copied_list = python_basic.list_copy([4, 3, 1, 5, 6])
    assert copied_list == [4, 3, 1, 5, 6]


@pytest.mark.benchmark
def test_list_append_benchmark(benchmark):
    """Benchmark the list_append function."""
    appended_list = benchmark(python_basic.list_append, thelist=[1, 2, 3, 4])
    assert appended_list == [[1, 2, 3, 4]]


@given(listInput=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_list_append_hypothesis(listInput):
    """Using hypothesis."""
    appended_list = python_basic.list_append(listInput)
    assert appended_list == [listInput]


@pytest.mark.parametrize(
    "list_input, expected_answer",
    [(2, [2]), (4, [4])],
)
def test_list_append_multiple(list_input, expected_answer):
    """Check the list_append function with multiple lists."""
    appended_list = python_basic.list_append(list_input)
    assert appended_list == expected_answer


def test_list_append_single():
    """Check the list_append function with a single list."""
    appended_list = python_basic.list_append(5)
    assert appended_list == [5]


def test_list_poplast_single():
    """Check the list_poplast function with a single list."""
    poplasted_list = python_basic.list_poplast([4, 3, 1, 5, 6])
    assert poplasted_list == [4, 3, 1, 5]


def test_list_in_single():
    """Check the list_in function with a single list."""
    list_is_in = python_basic.list_in([4, 3, 1, 5, 6], 4)
    list_isnot_in = python_basic.list_in([4, 3, 1, 5, 6], 10)
    assert list_is_in == 1
    assert list_isnot_in == 0


def test_dict_in_single():
    """Check the dict_in function with a single list."""
    dict_is_in = python_basic.dict_in({"first": 1, "second": 2, "third": 3}, "first")
    dict_isnot_in = python_basic.dict_in({"first": 1, "second": 2, "third": 3}, 1)
    assert dict_is_in == 1
    assert dict_isnot_in == 0
