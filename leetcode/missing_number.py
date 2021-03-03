"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        My solution
        :type nums: List[int]
        :rtype: int
        """
        num_sort = sorted(nums)
        counter = 1
        for i in range(num_sort[0], len(nums)+1):
            if counter not in nums:
                return counter
            elif counter == num_sort[0]:
                return 0
            counter+=1

    def missingNumber(self, nums):
        """
        Other solution
        """
        return int(*[x for x in range(0, len(nums) + 1) if x not in nums])
p = Solution()
print(p.missingNumber([3,0,1])) # 2
print( p.missingNumber([9,6,4,2,3,5,7,0,1])) # 8
print( p.missingNumber([1])) # 8
