"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""


class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        """My solution 32ms"""
        return "".join(word1) == "".join(word2)

p = Solution()
# print(p.smallerNumbersThanCurrent([6,5,4,8])) #  [2,1,0,3]
print(p.arrayStringsAreEqual(["ab", "c"],  ["a", "bc"]))  # 15