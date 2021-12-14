"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n):
        """Other leetcode solution"""
        if n <= 2: return n
        prev = 2
        prevofprev = 1
        current = 0
        for i in range(2,n):
            current = prev + prevofprev
            prevofprev = prev
            prev = current
        return current


    # """Other leetcode solution"""
    # def climbStairs(self, n):
    #     x, y = 0, 1
    #     for i in range(n):
    #         x, y = y, x + y
    #         print(x)
    #         print(y)
    #     return y


p = Solution()
print(p.climbStairs(2)) #2
print(p.climbStairs(5)) #3
#5
# 1+1+1+1+1
#1+2+2
#1+1+1+2
#1+2+1+1
#2+1+1+1
#2+2+1
#2+1+2