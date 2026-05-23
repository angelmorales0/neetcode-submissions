# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ret = head
        p1 = p2 = head
        prev  = None
        
        for _ in range(n):
            p2= p2.next
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next

        if not prev: # we reached end of list which ONLY happens whyen we pop first val 
            return ret.next

        prev.next = p1.next

        return ret 
        