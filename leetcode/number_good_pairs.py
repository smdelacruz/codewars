"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        Unfinished
        :type nums: List[int]
        :rtype: int
        """
        count=1
        num_pairs = []
        for i in range(len(nums)):
            for x in nums:
                if nums[i] == x:
                    num_pairs.append(x)
            # p = [x for x in nums if nummm == x]
p = Solution()
print(p.numIdenticalPairs([1,2,3,1,1,3])) # 4
print(p.numIdenticalPairs([1,1,1,1])) # 6