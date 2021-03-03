"""
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
"""


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        My solution
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        counter = []
        for i in words:
            p = all(x in allowed for x in i)
            counter.append(p)
        return counter.count(True)


p = Solution()
print(p.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
# print(p.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))