# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #temp = head

        #while head.next 
            #head == temp:
                #return True
            #head  move two nodes at a time 
            #move it once a time

        temp = head

        if head.next:
            head = head.next

        while head.next:
            if head == temp:
                return True
            head = head.next.next
            temp = temp.next
        return False



