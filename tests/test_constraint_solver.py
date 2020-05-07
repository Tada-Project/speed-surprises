"""Tests for the constraint solver function in the sets module of the lists package"""

import pytest

from speedsurprises.lists import sets


def test_CSP_basics_1_single():
    """Benchmark the CSP_basics_1 function"""
    solution = sets.CSP_basics_1([1, 2, 3], [4, 5, 6])
    expected = [{'a': 3, 'b': 6}, {'a': 3, 'b': 5}, {'a': 3, 'b': 4},
                {'a': 2, 'b': 6}, {'a': 2, 'b': 5}, {'a': 2, 'b': 4},
                {'a': 1, 'b': 6}, {'a': 1, 'b': 5}, {'a': 1, 'b': 4}]
    assert solution == expected


def test_CSP_basics_2_single():
    """Benchmark the CSP_basics_2 function"""
    solution = sets.CSP_basics_2([1, 2, 3], [4, 5, 6])
    expected = [{'a': 3, 'b': 6}, {'a': 2, 'b': 4}]
    assert solution == expected


def test_CSP_rooks_single():
    """Benchmark the CSP_rooks function"""
    cols = range(3)
    rows = range(3)
    solution = sets.CSP_rooks(cols, rows)
    expected = [{0: 2, 1: 1, 2: 0}, {0: 2, 1: 0, 2: 1}, {0: 1, 1: 2, 2: 0},
                {0: 1, 1: 0, 2: 2}, {0: 0, 1: 1, 2: 2}, {0: 0, 1: 2, 2: 1}]
    assert solution == expected
