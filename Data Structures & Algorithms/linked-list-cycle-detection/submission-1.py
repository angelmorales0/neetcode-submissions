# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        iterator = head
        node_set = set()

        while iterator != None:
            if iterator in node_set:
                return True
            else:
                node_set.add(iterator)
                iterator = iterator.next
        return False
        