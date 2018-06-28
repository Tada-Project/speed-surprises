"""Tests for the gatorgrader module"""

import pytest

from speedsurprises.text import copies


def test_correct_true_readable():
    """Ensures that the returned String is of correct length"""
    copied_character_string = copies.mcopies_ofc("10")
    print(copied_character_string)
