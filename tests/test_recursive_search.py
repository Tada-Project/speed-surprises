"""Tests for the recursive searching function in the recursive_search module of the search package"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from speedsurprises.search import recursive_search


@pytest.mark.benchmark
def test_recursive_binary_search_benchmark_found(benchmark):
    """Benchmark the recursive_binary_search function"""
    position = benchmark(
        recursive_search.compute_recursive_binary_search, list=[1, 2, 3, 4], x=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_recursive_binary_search_benchmark_notfound(benchmark):
    """Benchmark the recursive_binary_search function"""
    notfound = benchmark(
        recursive_search.compute_recursive_binary_search, list=[1, 2, 3, 4], x=10
    )
    assert notfound == -1


@pytest.mark.benchmark
def test_exponential_search_benchmark_found(benchmark):
    """Benchmark the exponential_search function"""
    position = benchmark(
        recursive_search.compute_exponential_search, list=[1, 2, 3, 4], x=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_exponential_search_benchmark_notfound(benchmark):
    """Benchmark the exponential_search function"""
    notfound = benchmark(
        recursive_search.compute_exponential_search, list=[1, 2, 3, 4], x=10
    )
    assert notfound == -1
