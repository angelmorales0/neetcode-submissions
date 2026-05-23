# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        builder = dummy
        seen = set()
        
        while head:
            last = head
            temp = head.next
            prev = last
            if head in seen:
                break

            while last.next:
                prev = last
                last = last.next
            prev.next = None
            builder.next = head
            seen.add(head)
            builder = builder.next 
            if last != head:
                seen.add(last)
                builder.next = last
                builder = builder.next
            head = temp

        head = dummy.next
        return 
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5.   6
        # H   
        #                          P    L

        #B -> 0 -> 1 -> L
            
            ##if count is even append
            #if odd go to end then apepend 
            


        #dummy and a dummyTemp to build