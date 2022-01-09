import math
class Solution:
    def sortedSquares(self, nums):
        return sorted([i ** 2 for i in nums])


p = Solution()
print(p.sortedSquares(nums = [-4,-1,0,3,10]))