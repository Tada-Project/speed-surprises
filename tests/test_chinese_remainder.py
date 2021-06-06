"""Tests for the chinese_remainder function in the sets module of the lists package."""

import pytest

from speedsurprises.lists import sets


@pytest.mark.benchmark
def test_chinese_remainder_benchmark(benchmark):
    """Benchmark the chinese_remainder function."""
    remainder = benchmark(sets.chinese_remainder, n=[3, 5, 7], a=[2, 3, 2])
    assert remainder == 23.0
