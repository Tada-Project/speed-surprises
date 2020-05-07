"""Tests for the constraint solver function in the sets module of the lists package"""

import pytest

from speedsurprises.lists import sets


@pytest.mark.benchmark
def test_CSP_basics_1_benchmark(benchmark):
    """Benchmark the CSP_basics_1 function"""
    solution = benchmark(
        sets.CSP_basics_1, a=[1, 2, 3], b=[4, 5, 6]
    )
    expected = [{'a': 3, 'b': 6}, {'a': 3, 'b': 5}, {'a': 3, 'b': 4},
                {'a': 2, 'b': 6}, {'a': 2, 'b': 5}, {'a': 2, 'b': 4},
                {'a': 1, 'b': 6}, {'a': 1, 'b': 5}, {'a': 1, 'b': 4}]
    assert solution == expected


@pytest.mark.benchmark
def test_CSP_basics_2_benchmark(benchmark):
    """Benchmark the CSP_basics_2 function"""
    solution = benchmark(
        sets.CSP_basics_2, a=[1, 2, 3], b=[4, 5, 6]
    )
    expected = [{'a': 3, 'b': 6}, {'a': 2, 'b': 4}]
    assert solution == expected


@pytest.mark.benchmark
def CSP_basics_3_benchmark(benchmark):
    """Benchmark the CSP_basics_3 function"""
    solution = benchmark(
        sets.CSP_basics_3, a=[1, 2, 3], b=[4, 5, 6]
    )
    expected = [{1: 6, 2: 5, 3: 4}, {1: 6, 2: 4, 3: 5}, {1: 5, 2: 6, 3: 4},
                {1: 5, 2: 4, 3: 6}, {1: 4, 2: 5, 3: 6}, {1: 4, 2: 6, 3: 5}]
    assert solution == expected


@pytest.mark.benchmark
def test_CSP_rooks_benchmark(benchmark):
    """Benchmark the CSP_rooks function"""
    solution = benchmark(
        sets.CSP_rooks, cols=range(3), rows=range(3)
    )
    expected = [{0: 2, 1: 1, 2: 0}, {0: 2, 1: 0, 2: 1}, {0: 1, 1: 2, 2: 0},
                {0: 1, 1: 0, 2: 2}, {0: 0, 1: 1, 2: 2}, {0: 0, 1: 2, 2: 1}]
    assert solution == expected
