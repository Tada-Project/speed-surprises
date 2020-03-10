"""Test for the one max problem with GA"""

import pytest
from speedsurprises.genetic_algorithm import onemax


@pytest.mark.parametrize(
    "input_amount, expected_answer", [(50, 50), (100, 100), (200, 200)],
)
def test_onemax_size_100(input_amount, expected_answer):
    """Test if onemax return all ones"""
    output = sum(onemax.onemax(input_amount))
    assert output == expected_answer
