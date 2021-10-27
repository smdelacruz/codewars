"""
Task
Let's call a string cool if it is formed only by Latin letters and no two lowercase
and no two uppercase letters are in adjacent positions. Given a string, check if it is cool.
Input/Output
[input] string s
A string that contains uppercase letters, lowercase letters numbers and spaces.
1 ≤ s.length ≤ 20.
[output] a boolean value
true if s is cool, false otherwise.
Example
For s = "aQwFdA", the output should be true
For s = "aBC", the output should be false;
For s = "AaA", the output should be true;
For s = "q q", the output should be false.
"""

import unittest
def cool_string(s):
    """
    Clever and best solution
    """
    return s.isalpha() and all(x.islower() != y.islower() for x, y in zip(s, s[1:]))


class Test_cool_string(unittest.TestCase):
    def test_results(self):
        self.assertEqual(cool_string("aQwFdA"), True)
        self.assertEqual(cool_string("aBC"), False)
        self.assertEqual(cool_string("AaA"), True)
        self.assertEqual(cool_string("q q"), False)
        self.assertEqual(cool_string("wWw1"), False)
        self.assertEqual(cool_string("2"), False)
        self.assertEqual(cool_string("aAaAaAa"), True)
        self.assertEqual(cool_string("    "), False)