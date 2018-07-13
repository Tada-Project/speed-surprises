"""Tests for the is_subset function in the sets module"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from speedsurprises.lists import sets


@pytest.mark.benchmark
def test_issubset_benchmark(benchmark):
    """Benchmark the is_subset function"""
    subset_found = benchmark(
        sets.is_subset, first_list=[1, 2, 3], second_list=[1, 2, 3, 4]
    )
    assert subset_found is True


@given(
    first_list=lists(elements=integers(min_value=1, max_value=5), min_size=0),
    second_list=lists(elements=integers(min_value=1, max_value=5), min_size=1),
)
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_issubset_hypothesis_integer_lists(first_list, second_list):
    """Returns output with correct factorial number"""
    fully_containing_list = [1, 2, 3, 4, 5]
    determined_is_subset_first = sets.is_subset(first_list, fully_containing_list)
    determined_is_subset_second = sets.is_subset(second_list, fully_containing_list)
    assert determined_is_subset_first is True
    assert determined_is_subset_second is True
