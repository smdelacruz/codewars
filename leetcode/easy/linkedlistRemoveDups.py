# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.headval = None

    def deleteDuplicates(self, head):
        print(head)
        head = self.headval
        print(head)
        if head.data == None:
            self.headval = head.next
            print(head)

            return
        # while head is not None:

llist = Solution()
llist.deleteDuplicates([1,1,2,3,3])