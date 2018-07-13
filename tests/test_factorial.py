"""Tests for the compute_factorial function in the numbers module"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from speedsurprises.numbers import factorial


@pytest.mark.benchmark
def test_factorial_benchmark(benchmark):
    """Benchmark the compute_factorial function"""
    computed_value = benchmark(factorial.compute_factorial, value=10)
    assert computed_value == 3628800


@given(factorial_input=integers(min_value=1, max_value=10))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_factorial_hypothesis(factorial_input):
    """Returns output with correct factorial number"""
    computed_value = factorial.compute_factorial(factorial_input)
    previous_computed_value = factorial.compute_factorial(factorial_input - 1)
    assert computed_value > 0
    assert previous_computed_value > 0
    assert computed_value == factorial_input * previous_computed_value


@pytest.mark.parametrize(
    "factorial_input,expected_answer",
    [(1, 1), (2, 2 * 1), (3, 3 * 2 * 1), (4, 4 * 3 * 2 * 1)],
)
def test_factorial_multiple(factorial_input, expected_answer):
    """Check the compute_factorial function with multiple inputs"""
    computed_value = factorial.compute_factorial(factorial_input)
    assert computed_value == expected_answer


def test_factorial_single():
    """Check the compute_factorial function with a single input"""
    computed_value = factorial.compute_factorial(10)
    assert computed_value == 3628800
