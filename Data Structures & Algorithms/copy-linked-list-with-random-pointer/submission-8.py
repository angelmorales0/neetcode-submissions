"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        if not head:
            return head
        map_node = head
        old_to_new = {}
        while map_node:
            new_node = Node(str(map_node.val),None,None)
            old_to_new[map_node] = new_node #now we map to the refernce 
            map_node = map_node.next

        ret = old = head

        while old:
            new = old_to_new[old]
            if old.next:
                new.next = old_to_new[old.next]
            if old.random:
                new.random = old_to_new[old.random]
            else:
                new.random = None
            old = old.next

        return old_to_new[head]





