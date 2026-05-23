"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapp = {}
        if node == None:
            return node
        def backtrack(node):
            if node in mapp:
                return mapp [node]

                
            new = Node(node.val)
            mapp[node] = new
            for nei in node.neighbors:
                new.neighbors.append(backtrack(nei))
            return new

        return backtrack(node)

