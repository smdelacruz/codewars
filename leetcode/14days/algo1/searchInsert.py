class Solution:
    def searchInsert(self, nums, target):
        if target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else:
            left = 0
            right = len(nums) -1 
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target: return pivot
                elif nums[pivot] > target:
                    right = pivot -1 
                else: 
                    left = pivot + 1
            return -1
            
            

p = Solution()
print(p.searchInsert(nums = [1,3,5,6], target = 7))