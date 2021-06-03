"""Tests for the compute_iterative_fibonacci and
compute_recursive_fibonacci functions in the
fibonacci module of the numbers package"""

import types
import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers

from speedsurprises.numbers import fibonacci


@pytest.mark.benchmark
def test_iterative_fibonacci_benchmark(benchmark):
    """Benchmark the compute_iterative_fibonacci function."""
    computed_iterative_value = benchmark(
        fibonacci.compute_iterative_fibonacci, value=19
    )
    assert computed_iterative_value == 4181


@pytest.mark.benchmark
def test_recursive_fibonacci_benchmark(benchmark):
    """Benchmark the compute_recusrive_fibonacci function."""
    computed_recursive_value = benchmark(
        fibonacci.compute_recursive_fibonacci, value=19
    )
    assert computed_recursive_value == 4181


@given(fibonacci_input=integers(min_value=2, max_value=10))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_fibonacci_hypothesis(fibonacci_input):
    """Returns output with correct fibonacci value."""
    computed_iterative_value = fibonacci.compute_iterative_fibonacci(fibonacci_input)
    computed_recursive_value = fibonacci.compute_recursive_fibonacci(fibonacci_input)
    previous_computed_iterative_value = fibonacci.compute_iterative_fibonacci(
        fibonacci_input - 1
    )
    previous_computed_recursive_value = fibonacci.compute_recursive_fibonacci(
        fibonacci_input - 1
    )
    goldenratio = 1.61803398875  # The golden ratio for fibonacci values.
    assert computed_iterative_value > 0
    if fibonacci_input <= 2:
        assert computed_iterative_value == 1
    else:
        assert computed_iterative_value == (
            # pylint: disable=W1633
            round(goldenratio * previous_computed_iterative_value)
        )
    assert computed_recursive_value > 0
    if fibonacci_input <= 2:
        assert computed_recursive_value == 1
    else:
        assert computed_recursive_value == (
            # pylint: disable=W1633
            round(goldenratio * previous_computed_recursive_value)
        )


@pytest.mark.parametrize(
    "fibonacci_input,expected_answer", [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5)],
)
def test_fibonacci_multiple(fibonacci_input, expected_answer):
    """Checks the iterative and recursive fibonacci functions with multiple inputs."""
    computed_iterative_value = fibonacci.compute_iterative_fibonacci(fibonacci_input)
    computed_recursive_value = fibonacci.compute_recursive_fibonacci(fibonacci_input)
    assert computed_iterative_value == expected_answer
    assert computed_recursive_value == expected_answer


def test_fibonacci_single():
    """Check the iterative and recursive fibonacci functions with a single input."""
    computed_iterative_value = fibonacci.compute_iterative_fibonacci(18)
    computed_recursive_value = fibonacci.compute_recursive_fibonacci(18)
    assert computed_iterative_value == 2584
    assert computed_recursive_value == 2584


def test_fibonacci_tuple():
    """Check the fibonacci function returns correct values in tuple."""
    computed_fibonacci_value = fibonacci.fibonacci_tuple(8)
    assert computed_fibonacci_value == (1, 1, 2, 3, 5, 8, 13, 21)


def test_fibonacci_list():
    """Check the fibonacci function returns correct values in list."""
    computed_fibonacci_value = fibonacci.fibonacci_list(8)
    assert computed_fibonacci_value == [1, 1, 2, 3, 5, 8, 13, 21]


def test_fibonacci_generator():
    """Check the fibonacci function returns generator."""
    computed_fibonacci_value = fibonacci.fibonacci_generator(8)
    assert isinstance(computed_fibonacci_value, types.GeneratorType) is True
