"""Tests for the mcopies_of function in the copies module"""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import text
from speedsurprises.text import copies

CHOSEN_LETTER = "X"


@pytest.mark.benchmark
def test_count_benchmark(benchmark):
    """Benchmark the mcopies_of function"""
    copied_character_string = benchmark(
        copies.mcopies_of, input_string="100", character=CHOSEN_LETTER
    )
    assert len(copied_character_string) == 100
    assert copied_character_string.count(CHOSEN_LETTER) == 100


@given(copies_as_int=integers(min_value=1), chosen_letter=text(min_size=1, max_size=1))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_letter_count_hypothesis(copies_as_int, chosen_letter):
    """Returns output with correct number of copies"""
    copy_count = copies_as_int
    copies_as_string = str(copies_as_int)
    copied_character_string = copies.mcopies_of(copies_as_string, chosen_letter)
    assert len(copied_character_string) == copy_count
    assert copied_character_string.count(chosen_letter) == copy_count


@pytest.mark.parametrize(
    "letter_count,expected_count,chosen_letter",
    [
        ("1", 1, CHOSEN_LETTER),
        ("10", 10, CHOSEN_LETTER),
        ("100", 100, CHOSEN_LETTER),
        ("1000", 1000, CHOSEN_LETTER),
    ],
)
def test_letter_count_multiple(letter_count, expected_count, chosen_letter):
    """Returns output with correct number of copies"""
    copied_character_string = copies.mcopies_of(letter_count, chosen_letter)
    assert len(copied_character_string) == expected_count
    assert copied_character_string.count(chosen_letter) == expected_count


def test_letter_count_single():
    """Returns output with correct number of copies"""
    copied_character_string = copies.mcopies_of("10", CHOSEN_LETTER)
    assert len(copied_character_string) == 10
    assert copied_character_string.count(CHOSEN_LETTER) == 10
