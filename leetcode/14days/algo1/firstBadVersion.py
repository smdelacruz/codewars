# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


# unlock solution

class Solution:
    def isBadVersion(self, bad):
        print("BAD", bad)
        if bad == 2: return True 
        else: return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n=5, bad =2
        left = 1
        right = n
        while left < right:
            middle = (left + right) //2 
            if self.isBadVersion(middle) is True: 
                right = middle
            else: 
                left = middle + 1
        return left


p = Solution()
print(p.firstBadVersion(2))