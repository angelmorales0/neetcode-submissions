# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.curr_max = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        def dfs(root, target):
            if not root:
                return False
            if root.val == target.val:
                return True 
            return dfs(root.left, target) or dfs(root.right, target)

        if dfs(root, p) and dfs(root, q):
            self.curr_max = root
            self.lowestCommonAncestor(root.left, p, q)
            self.lowestCommonAncestor(root.right,p, q)

        return self.curr_max
        #ordered
        #so smaller value must be to left or parent of greater value 

    