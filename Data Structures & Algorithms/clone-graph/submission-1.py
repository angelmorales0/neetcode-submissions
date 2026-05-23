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
            if not node or node in mapp:
                return 
        

            new = Node(node.val)
            mapp[node] = new

            for nei in node.neighbors:
                backtrack(nei)
        backtrack(node)
        for old in mapp:
            for nei in old.neighbors:
                mapp[old].neighbors.append(mapp[nei])

    
        for ret in mapp:
            return mapp[ret]

