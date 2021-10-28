"""
Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.

In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

Strings a and b may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).
If a and b have the same length treat a as the longer producing b+reverse(a)+b
"""

import unittest
def shorter_reverse_longer(a,b):
    """My solution"""
    if len(a) >= len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a
    return shorter + longer[::-1] + shorter


def shorter_reverse_longer(a,b):
    """Clever soltuion"""
    if len(a) < len(b): a, b = b, a
    return b+a[::-1]+b

def shorter_reverse_longer(a,b):
    """Other shorter precise solution"""
    return b + a[::-1] + b if len(a) >= len(b) else a + b[::-1] + a

class Testshorter_reverse_longer(unittest.TestCase):
    def test_results(self):

        self.assertEqual(shorter_reverse_longer("first", "abcde"), "abcdetsrifabcde")
        self.assertEqual(shorter_reverse_longer("hello", "bau"), "bauollehbau")
        self.assertEqual(shorter_reverse_longer("abcde", "fghi"), "fghiedcbafghi")
        self.assertEqual(shorter_reverse_longer("", ""), "")
        self.assertEqual(shorter_reverse_longer("", "aaaa"), "aaaa")
