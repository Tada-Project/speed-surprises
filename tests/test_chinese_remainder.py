"""Tests for the chinese_remainder function in the sets module of the lists package"""

import pytest

from speedsurprises.lists import sets


def test_chinese_remainder_single():
    """Benchmark the chinese_remainder function"""
    remainder = sets.chinese_remainder([3, 5, 7], [2, 3, 2])
    assert remainder == 23.0
