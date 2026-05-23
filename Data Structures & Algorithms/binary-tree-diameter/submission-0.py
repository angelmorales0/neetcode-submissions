# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curr_max = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal curr_max
            if not root:
                return -1 #height
            left = dfs(root.left)
            right = dfs(root.right)
            
            height = 2 + left + right
            curr_max = max(curr_max, height)

            return 1 + max(left, right)

        dfs(root)

        return curr_max
