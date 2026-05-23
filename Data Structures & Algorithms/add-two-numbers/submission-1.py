# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        places_map = {}
        count =1

        while l1 or l2:
            summ =0
            if l1:
                summ+= l1.val
                l1 = l1.next
            if l2:
                summ+= l2.val
                l2 = l2.next
            places_map[count]= summ
            count *=10
        ret_val = 0


        for key, val in places_map.items():
            ret_val += key*val

        prev = None
        ret_val = str(ret_val)
        for i in reversed(ret_val):
            newNode = ListNode(int(i))
            if not prev:
                ret = newNode
            if prev:
                prev.next = newNode 
            prev = newNode

            #enurmerate?
            #revrese

        return ret







        