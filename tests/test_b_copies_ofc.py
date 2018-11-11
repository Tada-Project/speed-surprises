"""Tests for the mcopies_ofc function in the copies module of the text package"""

import pytest

from speedsurprises.boolean import booleancopies


@pytest.mark.benchmark
def test_count_benchmark(benchmark):
    """Benchmark the mcopies_ofc function"""
    copied_boolean_list = benchmark(booleancopies.bcopies_ofc, inputlength="100")
    assert len(copied_boolean_list) == 100
    assert copied_boolean_list.count(True) == 100


@pytest.mark.parametrize(
    "boolean_count,expected_count", [("1", 1), ("10", 10), ("100", 100), ("1000", 1000)]
)
def test_boolean_count_multiple(boolean_count, expected_count):
    """Returns output with correct number of copies"""
    copied_boolean_list = booleancopies.bcopies_ofc(boolean_count)
    assert len(copied_boolean_list) == expected_count
    assert copied_boolean_list.count(True) == expected_count


def test_boolean_count_single():
    """Returns output with correct number of copies"""
    copied_boolean_list = booleancopies.bcopies_ofc("10")
    assert len(copied_boolean_list) == 10
    assert copied_boolean_list.count(True) == 10
