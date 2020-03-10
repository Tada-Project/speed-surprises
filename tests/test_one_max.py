"""Test for the one max problem with GA"""

from speedsurprises.genetic_algorithm import onemax


def test_onemax_size_100():
    """Test if onemax return all ones"""
    output = sum(onemax.onemax(100))
    expect = 100
    assert output == expect
