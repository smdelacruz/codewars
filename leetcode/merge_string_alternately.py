"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
"""


class Solution:
    def mergeAlternately(self, word1, word2):
        counter = 0
        # while counter != max(len(word1), len(word2)):
        #     if
        #     counter += 1
        new_word = ""
        for x in range(max(len(word1), len(word2))):
            print("x", x)
            print("1--", len(word1))
            print("2--", len(word2))
        #     try:
        #         if x % 2 == 0:
        #             new_word += word1[x] + word2[x]
        #     except IndexError as e:
        #         print("pass ", e)
        # return new_word

p = Solution()
# print(p.smallerNumbersThanCurrent([6,5,4,8])) #  [2,1,0,3]
# print(p.mergeAlternately("abc", "pqr"))  # apbqcr
print(p.mergeAlternately("ab", "pqrs"))  # apbqrs