"""Tests for the search function in the recursive_search module of the search package"""

import pytest

from speedsurprises.search import recursive_search


@pytest.mark.benchmark
def test_recursive_binary_search_benchmark_found(benchmark):
    """Benchmark the recursive_binary_search function"""
    position = benchmark(
        recursive_search.compute_recursive_binary_search, search_list=[1, 2, 3, 4], x=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_recursive_binary_search_benchmark_notfound(benchmark):
    """Benchmark the recursive_binary_search function"""
    notfound = benchmark(
        recursive_search.compute_recursive_binary_search, search_list=[1, 2, 3, 4], x=10
    )
    assert notfound == -1


@pytest.mark.benchmark
def test_exponential_search_benchmark_found(benchmark):
    """Benchmark the exponential_search function"""
    position = benchmark(
        recursive_search.compute_exponential_search, search_list=[1, 2, 3, 4], x=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_exponential_search_benchmark_notfound(benchmark):
    """Benchmark the exponential_search function"""
    notfound = benchmark(
        recursive_search.compute_exponential_search, search_list=[1, 2, 3, 4], x=10
    )
    assert notfound == -1
