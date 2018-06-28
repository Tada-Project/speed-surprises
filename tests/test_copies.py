"""Tests for the gatorgrader module"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from speedsurprises.text import copies

@pytest.mark.benchmark
def test_count_benchmark(benchmark):
    """Benchmark the mcopies_ofc function"""
    copied_character_string = benchmark(copies.mcopies_ofc, input_string="100")
    assert len(copied_character_string) == 100
    assert copied_character_string.count("C") == 100


@given(copies_as_int=integers(min_value=1))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_letter_count_hypothesis(copies_as_int):
    """Returns output with correct number of copies"""
    copy_count = copies_as_int
    copies_as_string = str(copies_as_int)
    copied_character_string = copies.mcopies_ofc(copies_as_string)
    assert len(copied_character_string) == copy_count
    assert copied_character_string.count("C") == copy_count


@pytest.mark.parametrize("letter_count,expected_count", [
    ("1", 1),
    ("10", 10),
    ("100", 100),
    ("1000", 1000),
])
def test_letter_count_multiple(letter_count, expected_count):
    """Returns output with correct number of copies"""
    copied_character_string = copies.mcopies_ofc(letter_count)
    assert len(copied_character_string) == expected_count
    assert copied_character_string.count("C") == expected_count


def test_letter_count_single():
    """Returns output with correct number of copies"""
    copied_character_string = copies.mcopies_ofc("10")
    assert len(copied_character_string) == 10
    assert copied_character_string.count("C") == 10
