"""
Unfinished
Given an array nums.
Return the running sum of nums.
Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""
class Solution:
    def runningSum(self,nums):
        """
        My solution
        """
        runningsum = []
        temp = 0
        for x in range(0, len(nums)):
            temp += nums[x]
            runningsum.append(temp)
        return runningsum


p = Solution()
print(p.runningSum([1,1,1,1,1])) # [1,2,3,4,5]
print(p.runningSum([1,2,3,4])) # [1,3,6,10]