# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        ret_node = root
        og = root
        curr_min = []

        
        def dfs(root):
            nonlocal count
            nonlocal ret_node
            
            curr_min.append(root)

            if root.left:
                dfs(root.left)
            count -= 1
            if count == 0:
                ret_node = root
                return root

            if root.right:
                dfs(root.right)  
        dfs(root)
        return ret_node.val

        