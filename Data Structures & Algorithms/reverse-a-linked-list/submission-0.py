# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        lastNode = None
        newHead = None

        while curr:
            nextNode = curr.next

            curr.next = lastNode
            lastNode = curr
            newHead = curr
            curr = nextNode
            
        return newHead
