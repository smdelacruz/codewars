# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        mergeList = list1 + list2
        sorted_list = sorted(list1 + list2)
        return sorted_list


p = Solution()
print(p.mergeTwoLists([1,2,3], [0]))
        