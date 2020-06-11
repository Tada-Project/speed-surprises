"""Tests for the compute_factorial function in the factorial module of the numbers package"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers

from speedsurprises.numbers import factorial


@pytest.mark.benchmark
def test_iterative_factorial_benchmark(benchmark):
    """Benchmark the compute_iterative_factorial function"""
    computed_value = benchmark(factorial.compute_iterative_factorial, value=10)
    assert computed_value == 3628800


@pytest.mark.benchmark
def test_recursive_factorial_benchmark(benchmark):
    """Benchmark the compute_recursive_factorial function"""
    computed_value = benchmark(factorial.compute_recursive_factorial, value=10)
    assert computed_value == 3628800


@pytest.mark.benchmark
def test_hashmap_recursive_factorial_benchmark(benchmark):
    """Benchmark the compute_hashmap_recursive_factorial function"""
    computed_value = benchmark(factorial.compute_hashmap_recursive_factorial, value=10)
    assert computed_value == 3628800


@given(factorial_input=integers(min_value=1, max_value=10))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_factorial_hypothesis(factorial_input):
    """Returns output with correct factorial number"""
    computed_iterative_value = factorial.compute_iterative_factorial(factorial_input)
    computed_recursive_value = factorial.compute_recursive_factorial(factorial_input)
    computed_hashmap_value = factorial.compute_hashmap_recursive_factorial(
        factorial_input
    )
    previous_computed_iterative_value = factorial.compute_iterative_factorial(
        factorial_input - 1
    )
    previous_computed_recursive_value = factorial.compute_recursive_factorial(
        factorial_input - 1
    )
    previous_hashmap_value = factorial.compute_hashmap_recursive_factorial(
        factorial_input - 1
    )
    assert computed_iterative_value > 0
    assert computed_recursive_value > 0
    assert computed_hashmap_value > 0
    assert previous_computed_iterative_value > 0
    assert previous_computed_recursive_value > 0
    assert previous_hashmap_value > 0
    assert (
        computed_iterative_value == factorial_input * previous_computed_iterative_value
    )
    assert (
        computed_recursive_value == factorial_input * previous_computed_recursive_value
    )
    assert computed_hashmap_value == factorial_input * previous_hashmap_value


@pytest.mark.parametrize(
    "factorial_input,expected_answer",
    [(1, 1), (2, 2 * 1), (3, 3 * 2 * 1), (4, 4 * 3 * 2 * 1)],
)
def test_factorial_multiple(factorial_input, expected_answer):
    """Check the compute_factorial function with multiple inputs"""
    computed_iterative_value = factorial.compute_iterative_factorial(factorial_input)
    computed_recursive_value = factorial.compute_recursive_factorial(factorial_input)
    computed_hashmap_value = factorial.compute_hashmap_recursive_factorial(
        factorial_input
    )
    assert computed_iterative_value == expected_answer
    assert computed_recursive_value == expected_answer
    assert computed_hashmap_value == expected_answer


def test_factorial_single():
    """Check the compute_factorial function with a single input"""
    computed_iterative_value = factorial.compute_iterative_factorial(10)
    computed_recursive_value = factorial.compute_recursive_factorial(10)
    computed_hashmap_value = factorial.compute_hashmap_recursive_factorial(10)
    assert computed_iterative_value == 3628800
    assert computed_recursive_value == 3628800
    assert computed_hashmap_value == 3628800


def test_error():
    """Check the compute_factorial function with a wrong input"""
    with pytest.raises(ValueError, match=r"Inputs of 0 or grater!"):
        computed_iterative_value = factorial.compute_iterative_factorial(-10)
        assert computed_iterative_value == 1
