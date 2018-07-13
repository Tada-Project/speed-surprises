"""Tests for the squareroot functions in the numbers module"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import floats
from speedsurprises.numbers import squareroot


@pytest.mark.benchmark
def test_squareroot_benchmark_bisection(benchmark):
    """Benchmark the squareroot functions"""
    computed_value_bisection = benchmark(
        squareroot.square_root_bisection, value=100, epsilon=0.001
    )
    assert computed_value_bisection == pytest.approx(10.0, 0.001)


@pytest.mark.benchmark
def test_squareroot_benchmark_exhaustive(benchmark):
    """Benchmark the squareroot functions"""
    computed_value_exhaustive = benchmark(
        squareroot.square_root_bisection, value=100, epsilon=0.001
    )
    assert computed_value_exhaustive == pytest.approx(10.0, 0.001)


@given(
    squareroot_input=floats(min_value=10.0, max_value=100.0),
    epsilon=floats(min_value=0.001, max_value=0.9999),
)
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_squareroot_bisection_hypothesis(squareroot_input, epsilon):
    """Returns output with correct squareroot value"""
    computed_value_bisection = squareroot.square_root_bisection(
        squareroot_input, epsilon
    )
    assert (
        pytest.approx(computed_value_bisection * computed_value_bisection, epsilon)
        == squareroot_input
    )


def test_squareroot_bisection_single():
    """Check the square_root_bisection function with a single input"""
    squareroot_input = 100.0
    epsilon = 0.001
    computed_value_bisection = squareroot.square_root_bisection(
        squareroot_input, epsilon
    )
    assert (
        pytest.approx(computed_value_bisection * computed_value_bisection, epsilon)
        == squareroot_input
    )
    assert pytest.approx(computed_value_bisection, epsilon) == 10.0


def test_squareroot_exchaustive_single():
    """Check the square_root_exhaustive function with a single input"""
    squareroot_input = 100.0
    epsilon = 0.001
    computed_value_exhaustive = squareroot.square_root_exhaustive(
        squareroot_input, epsilon
    )
    assert (
        pytest.approx(computed_value_exhaustive * computed_value_exhaustive, epsilon)
        == squareroot_input
    )
    assert pytest.approx(computed_value_exhaustive, epsilon) == 10.0
