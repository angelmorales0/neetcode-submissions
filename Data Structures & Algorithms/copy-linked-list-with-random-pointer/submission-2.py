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

        copy = {}
        h_r = head
        if not head:
            return head
        while h_r:
            copy[h_r] = Node(h_r.val)
            h_r = h_r.next

        cur = head
        while cur:
            cpy = copy[cur]
            copy[cur] = cpy # maps it to the copy node 
            cur = cur.next
        
        cur = head
        while cur:
            cpy = copy[cur]
            if cur.next:
                cpy.next = copy[cur.next]
            else:
                cpy.next = None
            if cur.random:
                cpy.random = copy[cur.random]
            else:
                cpy.random = None
            cur = cur.next
            

        return copy[head]
        