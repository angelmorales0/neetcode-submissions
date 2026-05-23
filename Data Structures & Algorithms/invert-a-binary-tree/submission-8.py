
        #def invert Tree
        #class Solution

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def invertTree(self, root):
        stack = []
        if not root: 
            return root
        stack.append(root)
        while stack:
            curr_node = stack.pop()
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
        return root 
        

        # 1
        #3 2 
        #