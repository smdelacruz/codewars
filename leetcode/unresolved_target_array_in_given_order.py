"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.
Example 1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
"""


class Solution:
    def createTargetArray(self, nums, indx):
        num_list = {}
        for i in range(len(nums)):
            num_list.update({nums[i]: indx[i]})
        return [k for k, v in sorted(num_list.items(), key=lambda x: x[1])]


p = Solution()
# print(p.smallerNumbersThanCurrent([6,5,4,8])) #  [2,1,0,3]
print(p.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))  # [0,4,1,3,2]