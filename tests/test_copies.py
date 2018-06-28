"""Tests for the gatorgrader module"""

import pytest

from speedsurprises.text import copies


def test_letter_count_single():
    """Returns output with correct number of copies"""
    copied_character_string = copies.mcopies_ofc("10")
    assert len(copied_character_string) == 10
    assert copied_character_string.count("C") == 10


@pytest.mark.parametrize("letter_count,expected_count", [
    ("10", 10),
    ("100", 100),
    ("1000", 1000),
])
def test_letter_count_multiple(letter_count, expected_count):
    """Check that it can detect zero or one paragraphs"""
    copied_character_string = copies.mcopies_ofc(letter_count)
    assert len(copied_character_string) == expected_count
    assert copied_character_string.count("C") == expected_count
