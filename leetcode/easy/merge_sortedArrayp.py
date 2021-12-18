class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        nums1 = nums2[:n]
        nums1.sort()
        print(nums1)
p = Solution()
print(p.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)) #5