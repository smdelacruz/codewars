"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""

import unittest
import pytest


def remove_exclamation_marks(s):
    return s.replace("!", "")


def test_remove_exclamation_marks():
    """
    command pytest __filename__ -v
    """
    assert remove_exclamation_marks('Hello World!') == "Hello World"
    assert remove_exclamation_marks("") == ""



# class Testthis(unittest.TestCase):
#     """
#     command python -m unittest __filename__ -v
#     """
#     def test_remove_exclamation_marks(self):
#         self.assertEqual(remove_exclamation_marks('Hello World!'), "Hello World")
#         self.assertEqual(remove_exclamation_marks(''), "")
#         self.assertEqual(remove_exclamation_marks('Hello! There! My ! Friend'), "Hello There My  Friend")

