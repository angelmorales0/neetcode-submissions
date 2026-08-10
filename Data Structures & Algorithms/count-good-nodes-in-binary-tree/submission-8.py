# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,stack,maxStack):
            nonlocal goodNodes
            if not node:
                return 
            if not stack or maxStack <= node.val:
                goodNodes +=1 
            if node.val >= maxStack:
                maxStack = node.val

            stack.append(node.val)

            dfs(node.left,stack,maxStack)
            dfs(node.right,stack,maxStack)
            stack.pop()

        goodNodes = 0
     
        dfs(root,[],float('-inf'))
        return goodNodes

        

