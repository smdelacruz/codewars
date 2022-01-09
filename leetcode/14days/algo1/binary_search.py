
"""
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
class Solution:
    def search(self, nums, target):
        """240ms 48.7% """
        # if target not in nums: 
        #     return -1
        # else: 
        #     for i, v in enumerate(nums):
        #         if v == target:
        #             return i

        """
        solution using O(log N) pivot
        because it is a sorted array
        236ms, 65.94%
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if target == nums[pivot]:
                return pivot
            elif target > nums[pivot]:
                left = pivot+1
            else:
                right = pivot -1
        return -1

p = Solution()
print(p.search(nums = [-1,0,3,5,9,12], target = 9)) #4