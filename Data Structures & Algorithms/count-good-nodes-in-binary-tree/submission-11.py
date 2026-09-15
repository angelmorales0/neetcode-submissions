# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def dfs(node,maxSeen):
            nonlocal goodNodes
            if node.left:
                dfs(node.left, max(maxSeen, node.val))
            if node.right:
                dfs(node.right, max(maxSeen, node.val))

            if maxSeen <= node.val:
                goodNodes +=1

        dfs(root,root.val)
        return goodNodes