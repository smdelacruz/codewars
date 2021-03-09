"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
"""


class Solution:
    def subtractProductAndSum(self, n):
        """My solution 16ms"""
        theprod = 1
        thesum = 0
        for i in str(n):
            thesum = thesum + int(i)
            theprod = theprod * int(i)
        return theprod - thesum

    def subtractProductAndSum(self, n: int) -> int:
        """
        short solution from leetcode
        """
        if n == 1:
            return 0
        arr = list(str(n))
        summ = reduce((lambda x, y: int(x) + int(y)), arr)
        prod = reduce((lambda x, y: int(x) * int(y)), arr)
        return prod - summ


    """ Other solution from leetcode using math.prod"""
from math import prod

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_list = [int(x) for x in str(n)]
        return prod(num_list) - sum(num_list)
    
p = Solution()
# print(p.smallerNumbersThanCurrent([6,5,4,8])) #  [2,1,0,3]
print(p.subtractProductAndSum(234))  # 15