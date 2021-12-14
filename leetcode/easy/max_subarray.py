"""
A subarray is a contiguous part of an array.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    def maxSubArray(self, nums):
        #previous = -1
        # i = -3
        #sum_counter = -2 + 1 = -1
        max_list = []
        previous = nums[0]
        sum_counter = 0
        for i in nums[1:]:
            print("current data", i)
            if sum_counter < 0:
                sum_counter = previous + i
                previous = sum_counter
            else: pass


