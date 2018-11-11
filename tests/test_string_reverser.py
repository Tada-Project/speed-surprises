"""Tests for the string_reverser function in the copies module of the text package"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers

from speedsurprises.text import string_reverser


@pytest.mark.benchmark
def test_string_reverser_benchmark(benchmark):
    """Benchmark the mcopies_of function"""
    reversed_bnch_string = benchmark(
        string_reverser.reverse, s="hello",
    )
    assert len(reversed_bnch_string) == 5
    assert reversed_bnch_string == "olleh"


@given(input_string=string(elements=integers(min_value=1, max_value=5), min_size=3))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_issubset_hypothesis_integer_lists_yes(input_string):
    """Returns output with reversed string number"""
    function_reversed_string = string_reverser.reverse(input_string)
    python_reversed_string = input_string[::-1]
    assert function_reversed_string == python_reversed_string


@pytest.mark.parametrize(
    "original_string, reversed_string",
    [
        ("tester", "retset"),
        ("hello", "olleh"),
    ],
)
def test_string_reverser_multiple(original_string, reversed_string):
    """Returns multiple reversed strings"""
    function_reversed_string = string_reverser.reverse(original_string)
    assert function_reversed_string == reversed_string


def test_string_reverser_single():
    """Returns single reversed string"""
    function_reversed_string = string_reverser.reverse("welcome")
    assert function_reversed_string == "emoclew"
