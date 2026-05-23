# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        iterator = head
        node_set = {}

        while iterator != None:
            node_set[iterator] = node_set.get(iterator, 0) + 1
            if node_set[iterator] > 1:
                return True
            else:
                iterator = iterator.next
        return False
        