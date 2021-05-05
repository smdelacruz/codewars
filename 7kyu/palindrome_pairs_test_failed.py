"""
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list so that the concatenation of
the two words, i.e. words[i] + words[j] is a palindrome.

Examples:

["bat", "tab", "cat"] # [[0, 1], [1, 0]]
["dog", "cow", "tap", "god", "pat"] # [[0, 3], [2, 4], [3, 0], [4, 2]]
["abcd", "dcba", "lls", "s", "sssll"] # [[0, 1], [1, 0], [2, 4], [3, 2]]
Non-string inputs should be converted to strings.

Return an array of arrays containing pairs of distinct indices that form palindromes.
Pairs should be returned in the order they appear in the original list.

Test Failed = https://www.codewars.com/kata/5772ded6914da62b4b0000f8/discuss
"""
import unittest
def palindrome_pairs(words):
    palidrome = []
    for k,v in enumerate(words):
        w1 = "".join(sorted(v))
        for k1,v2 in enumerate(words):
            w2 = "".join(sorted(v2))
            if w1 == w2 and k != k1:
                palidrome.append([k, k1])
    return palidrome
print(palindrome_pairs(["bat", "tab", "cat"]))


class Test_palindrome_pairs(unittest.TestCase):
  def test_results(self):
      self.assertEqual(palindrome_pairs(["bat", "tab", "cat"]), [[0, 1], [1, 0]])
      self.assertEqual(palindrome_pairs(["dog", "cow", "tap", "god", "pat"]), [[0, 3], [2, 4], [3, 0], [4, 2]])