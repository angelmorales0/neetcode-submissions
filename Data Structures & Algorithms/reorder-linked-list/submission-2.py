# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first we want to find half 
        L = head
        R = head
        while R != None and R.next != None:
            R = R.next.next
            L = L .next
        #L increases by 1 for every 2x increase of R so L and down is middle
        start_2 = L.next
        L.next = None


        #Now we ust reverses our second half of linked list 
        if start_2 != None:
            temp = start_2.next
            start_2.next = None
        else:
            temp = start_2
            
        while temp != None:
            temp2 = temp.next
            temp.next= start_2
            start_2 = temp
            temp = temp2
        #reverses the list 
        #start 2 = head of reversed list 
        L_head = head

        while start_2 != None and L_head != None:

            L_temp = L_head.next
            R_temp = start_2.next

            L_head.next = start_2
            start_2.next = L_temp
            start_2 = R_temp
            L_head = L_temp




