# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #run dfs on every node as the root:
        #compute 2 values one without splitting  + sibling node path and one with splitting
        ret= root.val

        #returns max sum without spliting
        def dfs(node):
            nonlocal ret
            print(ret)
            if not node:
                return 0
            #get the max of the paths
            left_max = max(0,dfs(node.left))
            right_max  = max(0,dfs(node.right))

            #with split since this node is our 'root' for the path 
            ret= max(ret, node.val + left_max+right_max)

            return node.val + max(left_max,right_max)

        dfs(root)
        return ret