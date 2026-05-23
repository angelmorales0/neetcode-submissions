# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)

        L = dummy_node
        R = head

        while n > 0:
            R = R.next
            n -= 1

        while R != None:
            R= R.next
            L= L.next
        L.next = L.next.next
        return dummy_node.next