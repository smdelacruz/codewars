"""
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

class Solution:
    def removeElement(self, nums, val):
        # my solution 1 - trasnfer elemtn to another array - working but incorrect
        # new_nums = []
        # nums_len = len(nums)
        # for i in range(nums_len):
        #     print(nums[i])
        #     if nums[i] != val:
        #         new_nums.append(nums[i])
        # print(new_nums)
        # return len(new_nums)

        # my solution 2 - remove the element, not use new array - working but incorrect
        # nums_len = len(nums)
        # for i in range(nums_len):
        #     if nums[i] == val:
        #         nums[i] = "_"
        # return len([i for i in nums if type(i) == int])

        # my solution 3
        # for i in nums[:]: #copy
        #     if val == i:
        #         nums.remove(i)
        # return nums


        #other people's solution
        # x = nums.count(val) #first he get the total number of val exist in nums
        # for i in range(x): #loop for example only 2 times
        #     nums.remove(val) #remove the val every loop
        # return nums

        #other people's solution # easiest solution
        while val in nums:
            nums.remove(val)
            print(nums)
        return nums

p = Solution()
print(p.removeElement([0,0,2,0], 0))
# print(p.removeElement([3,2,2,3], 3))
        