"""
Given a number, find the permutation with the smallest absolute value (no leading zeros).

-20 => -20
-32 => -23
0 => 0
10 => 10
29394 => 23499
The input will always be an integer.
"""
import unittest
def min_permutation(n):
    """
    Unresolved
    BEst solution in Kata
    """
    f = n < 0
    s = "".join(sorted(str(abs(n))))
    n = s.count("0")
    s = s.replace("0", "")
    return int(s[:1] + "0" * n + s[1:]) * (-1 if f else 1)

print(min_permutation(-200))
print(min_permutation(-92))
# class Test_min_permutation(unittest.TestCase):
#     def test_results(self):
#         self.assertEqual(min_permutation(-20),-20)