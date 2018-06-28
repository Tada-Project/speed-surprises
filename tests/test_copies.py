"""Tests for the gatorgrader module"""

from speedsurprises.text import copies


def test_correct_true_readable():
    """Returns output with correct number of copies"""
    copied_character_string = copies.mcopies_ofc("10")
    assert len(copied_character_string) == 10
    assert copied_character_string.count("C") == 10
