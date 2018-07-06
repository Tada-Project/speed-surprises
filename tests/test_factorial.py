"""Tests for the compute_factorial function in the numbers module"""

import pytest

# from hypothesis import given
# from hypothesis import settings
# from hypothesis import Verbosity
# from hypothesis.strategies import integers
from speedsurprises.numbers import factorial


@pytest.mark.benchmark
def test_count_benchmark(benchmark):
    """Benchmark the compute_factorial function"""
    computed_value = benchmark(factorial.compute_factorial, value=10)
    assert computed_value == 3628800
