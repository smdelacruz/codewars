"""
Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
"""


class Solution(object):
    def findNumbers(self, nums):
        """
        Unfinished
        :type nums: List[int]
        :rtype: int
        """
        return len([i for i in nums if len(str(i)) % 2 == 0])
p = Solution()
p.findNumbers([555,901,482,1771]) # 1 . 1771 = 4digit which is even