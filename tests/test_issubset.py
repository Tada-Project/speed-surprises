"""Tests for the is_subset function in the sets module"""

import pytest

from speedsurprises.lists import sets


@pytest.mark.benchmark
def test_count_benchmark(benchmark):
    """Benchmark the compute_factorial function"""
    subset_found = benchmark(
        sets.is_subset, first_list=[1, 2, 3], second_list=[1, 2, 3, 4]
    )
    assert subset_found is True
