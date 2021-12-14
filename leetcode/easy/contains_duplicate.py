class Solution:
    def containsDuplicate(self, nums):
        # my solution
        no_dupliate = list(set(nums))
        print(sorted(no_dupliate))
        print(sorted(nums) )
        return sorted(no_dupliate) != sorted(nums)

        """
        other leetcode solution
        """
        return len(set(nums)) != len(nums)


p = Solution()
print(p.containsDuplicate([0,0,1,1,1,2,2,3,3,4]))
        