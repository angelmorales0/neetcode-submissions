# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        depth = 1
        curr_max = 0
        if not root:
            return 0
        stack.append([root, depth])


        while stack != []:
            node, depth = stack.pop()
            curr_max = max(curr_max, depth)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        return curr_max


        