"""Tests for the recursive searching function in the recursive_search module of the search package"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from speedsurprises.search import recursive_search


@pytest.mark.benchmark
def test_recursive_binary_search_benchmark(benchmark):
    """Benchmark the recursive_binary_search function"""
    position = benchmark(
        recursive_search.compute_recursive_binary_search, list=[4, 2, 3, 1], x=4
    )
    notfound = benchmark(
        recursive_search.compute_recursive_binary_search, list=[4, 2, 3, 1], x=10
    )
    assert position == 0
    assert notfound == -1


@pytest.mark.benchmark
def test_exponential_search_benchmark(benchmark):
    """Benchmark the exponential_search function"""
    position = benchmark(
        recursive_search.compute_exponential_search, list=[4, 2, 3, 1], x=4
    )
    notfound = benchmark(
        recursive_search.compute_exponential_search, list=[4, 2, 3, 1], x=10
    )
    assert position == 0
    assert notfound == -1
