# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #add values in order to array then return k-1st index 

        #while you can go left go left -> then add to array
        #then add parent to array 
            #if possible to go right go right nad repeat 
        def dfs(node):
            nonlocal ret
            if node.left:
                dfs (node.left) #stops at final val
            ret.append(node.val)
            if node.right:
                dfs(node.right)
            

        ret = []
        dfs(root)
        return ret[k-1]
            
       

