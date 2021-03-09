"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        """
        My Solution 52ms
        """
        new_list = []
        for val in nums:
            counter = 0
            for i in range(len(nums)):
                if val > nums[i]:
                    counter += 1
            new_list.append(counter)
        return new_list

    def smallerNumbersThanCurrent(self, nums):
        """
        Clever answer from leetcode
        """
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]
p = Solution()
# print(p.smallerNumbersThanCurrent([6,5,4,8])) #  [2,1,0,3]
print(p.smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]

