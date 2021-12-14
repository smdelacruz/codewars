class Solution:
    def removeDuplicates(self, nums):
        """
        my soltuion
        """
        # temp = []
        # for i in nums[:]:
        #     if i not in temp:
        #         temp.append(i)
        #     else:
        #         nums.remove(i)
        # return len(nums)

        #other solution
        duplicates = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: 
                duplicates += 1
            else:
                nums[i - duplicates] = nums[i]

        return len(nums) - duplicates


p = Solution()
print(p.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        