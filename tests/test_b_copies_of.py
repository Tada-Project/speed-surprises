"""Tests for the bcopies_of function in the copies module of the text package"""

import pytest

from speedsurprises.boolean import booleancopies

CHOSEN_BOOLEAN = True


@pytest.mark.benchmark
def test_count_benchmark(benchmark):
    """Benchmark the bcopies_of function"""
    copied_boolean_list = benchmark(
        booleancopies.bcopies_of, inputlength="100", boolean=CHOSEN_BOOLEAN
    )
    assert len(copied_boolean_list) == 100
    assert copied_boolean_list.count(CHOSEN_BOOLEAN) == 100


@pytest.mark.parametrize(
    "boolean_count,expected_count,chosen_boolean",
    [
        ("1", 1, CHOSEN_BOOLEAN),
        ("10", 10, CHOSEN_BOOLEAN),
        ("100", 100, CHOSEN_BOOLEAN),
        ("1000", 1000, CHOSEN_BOOLEAN),
    ],
)
def test_boolean_count_multiple(boolean_count, expected_count, chosen_boolean):
    """Returns output with correct number of copies"""
    copied_boolean_list = booleancopies.bcopies_of(boolean_count, chosen_boolean)
    assert len(copied_boolean_list) == expected_count
    assert copied_boolean_list.count(chosen_boolean) == expected_count


def test_boolean_count_single():
    """Returns output with correct number of copies"""
    copied_boolean_list = booleancopies.bcopies_of("10", CHOSEN_BOOLEAN)
    assert len(copied_boolean_list) == 10
    assert copied_boolean_list.count(CHOSEN_BOOLEAN) == 10
