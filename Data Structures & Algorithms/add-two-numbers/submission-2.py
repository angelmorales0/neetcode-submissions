# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ret = ListNode(0)

        while l1 or l2 or (carry > 0):
            summ = 0
            if carry > 0:
                summ = carry
                carry = 0
            
            if l1:
                summ += l1.val
            if l2:
                summ += l2.val
            while summ >= 10:
                carry +=1
                summ -=10
            dummy.next = ListNode(summ)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ret.next
            
            
            
        