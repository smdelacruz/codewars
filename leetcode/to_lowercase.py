"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
"""


class Solution:
    def toLowerCase(self, str):
        return str.lower()


p = Solution()
# print(p.smallerNumbersThanCurrent([6,5,4,8])) #  [2,1,0,3]
print(p.toLowerCase("Hello"))  # hello
print(p.toLowerCase("LOVELY"))  # lovely