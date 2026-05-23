# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        if head:
            head = head.next
        if dummy:
            dummy.next = None

        while head:
            temp = head.next
            head.next = dummy 
            dummy = head
            head = temp
        return dummy
        # _ <- 1 -> 2 -> _
        #. D    H    T   H
        #1
        