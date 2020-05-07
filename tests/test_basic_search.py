"""Tests for the basic searching function in the basic_search module of the search package"""

import pytest

from speedsurprises.search import basic_search


@pytest.mark.benchmark
def test_linear_search_benchmark_found(benchmark):
    """Benchmark the insertionSort function"""
    position = benchmark(
        basic_search.compute_linear_search, list=[1, 2, 3, 4], x=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_linear_search_benchmark_notfound(benchmark):
    """Benchmark the insertionSort function"""
    notfound = benchmark(
        basic_search.compute_linear_search, list=[1, 2, 3, 4], x=10
    )
    assert notfound == -1


@pytest.mark.benchmark
def test_iterative_binary_search_benchmark_found(benchmark):
    """Benchmark the iterative_binary_search function"""
    position = benchmark(
        basic_search.compute_iterative_binary_search, list=[1, 2, 3, 4], target=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_iterative_binary_search_benchmark_notfound(benchmark):
    """Benchmark the iterative_binary_search function"""
    notfound = benchmark(
        basic_search.compute_iterative_binary_search, list=[1, 2, 3, 4], target=10
    )
    assert notfound == -1


@pytest.mark.benchmark
def test_jump_search_benchmark_found(benchmark):
    """Benchmark the jump_search function"""
    position = benchmark(
        basic_search.compute_jump_search, list=[1, 2, 3, 4], x=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_jump_search_benchmark_notfound(benchmark):
    """Benchmark the jump_search function"""
    notfound = benchmark(
        basic_search.compute_jump_search, list=[1, 2, 3, 4], x=10
    )
    assert notfound == -1


@pytest.mark.benchmark
def test_compute_interpolation_search_benchmark_found(benchmark):
    """Benchmark the interpolation_search function"""
    position = benchmark(
        basic_search.compute_interpolation_search, list=[1, 2, 3, 4], x=2
    )
    assert position == 1


@pytest.mark.benchmark
def test_compute_interpolation_search_benchmark_notfound(benchmark):
    """Benchmark the interpolation_search function"""
    notfound = benchmark(
        basic_search.compute_interpolation_search, list=[1, 2, 3, 4], x=10
    )
    assert notfound == -1
