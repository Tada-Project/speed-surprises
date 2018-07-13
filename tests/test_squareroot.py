"""Tests for the squareroot functions in the numbers module"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import floats
from speedsurprises.numbers import squareroot


@pytest.mark.benchmark
def test_squareroot_benchmark(benchmark):
    """Benchmark the squareroot functions"""
    # squareroot.square_root_bisection(100, 0.0001)
    computed_value = benchmark(squareroot.square_root_bisection, value=100, epsilon=0.001)
    assert computed_value == pytest.approx(10.0, 0.001)
