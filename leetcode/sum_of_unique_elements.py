"""
You are given an integer array nums.
The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
"""


class Solution:
    def sumOfUnique(self, nums):
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
                print("uniq", unique)
            else:
                print("duplicate ", i)
                unique.remove(i)
        print(unique)
        # return sum[unique]

p = Solution()
# print(p.smallerNumbersThanCurrent([6,5,4,8])) #  [2,1,0,3]
print(p.sumOfUnique([1,2,3,2]))  #4
print(p.sumOfUnique([1,1,1,1,1]))  #0