# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #first idea is go. thru all lists -> sort -> go thru array and return 
        #build list by moving head pointer 
        #how tf do I move head pointer 

        ret = newHead = ListNode()

        while lists:
            minHead = ListNode(float('inf'))
            minIndex = 0
            for i in range(len(lists)):
                linkedListHead = lists[i]
                if not linkedListHead: #no linked list head
                    lists.pop(i)
                    minHead = ListNode(float('inf'))
                    break

                elif linkedListHead.val < minHead.val:
                    minHead = linkedListHead
                    minIndex = lists.index(linkedListHead)

            if minHead.val != float('inf'):
                lists[minIndex] = lists[minIndex].next #moves to next
                minHead.next = None
                newHead.next = minHead
                newHead = newHead.next

        return ret.next 
        