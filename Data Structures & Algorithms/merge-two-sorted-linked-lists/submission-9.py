# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return list1

        if list1 == None:
            f_head = list2
            list2 = list2.next
            curr = f_head
        elif list2 == None:
            f_head= list1
            list1 = list1.next
            curr = f_head
        elif list1.val <= list2.val:
            f_head= list1
            list1 = list1.next
            curr = f_head
        else:
            f_head = list2
            list2 = list2.next
            curr = f_head

        while list1 != None or list2 != None:
            if list1 == None:
                curr.next = list2
                break

            elif list2 == None:
                curr.next = list1
                break
            elif list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next

            else:
                curr.next = list2
                curr = curr.next
                list2=list2.next

        return f_head

        

