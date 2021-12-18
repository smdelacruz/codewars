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
        highest = nums[0]
        sum_counter = 0
        for i in nums[1:]:
            if sum_counter < 0:
                sum_counter = 0
            sum_counter += i
            print("n=, ", i)
            print("sum_counter, ", sum_counter)
            highest = max(sum_counter, highest)
        return highest

p = Solution()
print(p.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #5
print(p.maxSubArray([-2])) #5

