# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #run merge sort type shit 
        if len(lists) ==0 :
            return ListNode().next
        def merge(list1, list2):
            dummy= dh = ListNode()
            while list1 and list2:
                if list1.val< list2.val:
                    dh.next = list1
                    dh = dh.next
                    list1=list1.next
                else:
                    dh.next = list2
                    dh = dh.next
                    list2=list2.next
            if list2:
                dh.next = list2
            if list1:
                dh.next = list1
            return dummy.next
        i = 0 
        
        while len(lists) > 1:
            newList = merge(lists[i],lists[i+1])
            lists.pop(i+1)
            lists[i] = newList
        return lists[0]
       

