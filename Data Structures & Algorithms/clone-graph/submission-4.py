"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew ={}
        if not node:
            return node
        def clone(node):
            if node in oldToNew: #if already exists in mapping just return it (since we go back to it multiple times)
                return oldToNew[node]
            else:
                newNode = Node(node.val)
                oldToNew[node] = newNode #add it to the clone list 

            for neighbor in node.neighbors: #clone the neighbors and append it 
                newNode.neighbors.append(clone(neighbor))

            return newNode #rturn our cloned node 
        clone(node)
        return oldToNew[node]