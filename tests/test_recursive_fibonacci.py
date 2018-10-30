"""Tests for the compute_recursive_fibonacci function in the
fibonacci module of the numbers package"""

import math
import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers

from speedsurprises.numbers import fibonacci


@pytest.mark.benchmark
def test_recursive_fibonacci_benchmark(benchmark):
    """Benchmark the compute_recursive_fibonacci function"""
    computed_value = benchmark(fibonacci.compute_recursive_fibonacci, value=19)
    assert computed_value == 4181


@given(fibonacci_input=integers(min_value=2, max_value=10))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_fibonacci_hypothesis(fibonacci_input):
    """Returns output with correct fibonacci value"""
    computed_value = fibonacci.compute_recursive_fibonacci(fibonacci_input)
    previous_computed_value = (
        fibonacci.compute_recursive_fibonacci(fibonacci_input - 1)
    )
    goldenratio = 1.61803398875  # The golden ratio for fibonacci values.
    assert computed_value > 0
    assert computed_value == (
        math.ceil(goldenratio * previous_computed_value)
    )


@pytest.mark.parametrize(
    "fibonacci_input,expected_answer",
    [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5)],
)
def test_fibonacci_multiple(fibonacci_input, expected_answer):
    """Check the compute_recursive_fibonacci function with multiple inputs"""
    computed_value = fibonacci.compute_recursive_fibonacci(fibonacci_input)
    assert computed_value == expected_answer


def test_fibonacci_single():
    """Check the compute_recursive_fibonacci function with a single input"""
    computed_value = fibonacci.compute_recursive_fibonacci(18)
    assert computed_value == 2584
