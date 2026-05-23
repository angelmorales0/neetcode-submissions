# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy_node = ListNode(0,head)
        L = dummy_node 
        R = head
        while count < n:
            R = R.next
            count += 1 # gets R N+1 values away from L

        while R != None:
            R = R.next
            L = L.next
        #noew L is 1 before skippable index 
        
        L.next = L.next.next

        return dummy_node.next
    

    