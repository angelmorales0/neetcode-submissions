# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ret= dummy = ListNode(0)
        while l1 or l2 or carry > 0:
            tot = 0
            if l1:
                tot+=l1.val
                l1 = l1.next
            if l2:
                tot += l2.val
                l2 = l2.next

            if carry >0: #adds carry
                tot += carry
                carry = 0
            
            while tot >= 10: #makes carry if needed
                tot -=10
                carry +=1
            dummy.next = ListNode(tot)
            dummy = dummy.next
        return ret.next
            



        