# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True
        l_bound = float('-inf')
        r_bound = float('inf')


        def dfs(root, l, r):
            nonlocal is_valid
      
            if root.val >= r or root.val <= l:
                is_valid = False

            if root.left:
                dfs(root.left,l, root.val)

            if root.right:
                dfs(root.right, root.val, r)
            
        dfs(root, l_bound, r_bound)
        return is_valid
            

        