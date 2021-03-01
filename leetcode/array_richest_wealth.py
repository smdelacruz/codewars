def maximumWealth(accounts):
    """
    My solution 52ms
    """
    sort_acc = sorted([sum(i) for i in accounts], reverse=True)[0]
    return sort_acc
    
"""
Other solutions
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts))
 class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(a) for a in accounts])
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(a) for a in accounts)

"""


accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maximumWealth(accounts))
        