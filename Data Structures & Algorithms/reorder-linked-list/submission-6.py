# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(start):
            p= None
            h = start
            while h:
                temp = h.next
                h.next = p
                p =h
                h=temp
            return p

        s = f = head
        while f.next and f.next.next: #double next is for even case 
            f = f.next.next
            s=s.next 
        l2 = s.next
        l2 = reverse(l2)
 

        s.next = None # to let us split the list 

        #Need to MERGE The 2 lists l2  in place??
        ret = head
        while head:
            temp = head.next
            if l2:
                temp2 = l2.next
            else:
                temp2 = None
            head.next = l2
            if l2:
                l2.next = temp
            head = temp 
            l2= temp2
        head = ret
        return 
