class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums_len = len(nums)
        # copy_nums = nums
        # for i , v in enumerate(copy_nums):
        #     print("current v", v)
        #     # index_sum = i + k
        #     # if index_sum <= (nums_len -1):
        #     #     nums[index_sum] = v
        #     # else: 
        #     #     diff = index_sum - nums_len
        #     #     nums[diff] = v
        # return nums
        sliced = len(nums) - k
        print(sliced)
        a3 = nums[sliced:]
        
        temp1 = nums[:k]
        # a2 = nums[k:]
        print(temp1)
        # print(a2)
        print(a3)
        # temp2 = list(set(nums) - set(temp1))
        # print(temp1)
        # print(temp2)
        # nums = temp2 + temp1
        # return nums

p = Solution()
print(p.rotate(nums = [-1,-100,3,99], k=2)) #[3,99,-1,-100]
print(p.rotate(nums = [1,2,3,4,5,6,7], k=3)) #[5,6,7,1,2,3,4]