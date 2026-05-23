# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = [] 
        ret = []

        level = 1
        if not root:
            return []

        q.append([root, level])

        while q:
            curr = q.pop()

            if curr[1]-1 in range(len(res)):
                res[curr[1]-1].append(curr[0].val)
            else:
                res.append([curr[0].val])

            if curr[0].left:
                q.appendleft([curr[0].left, curr[1]+1]) 
            if curr[0].right:
                q.appendleft([curr[0].right, curr[1]+1])



        return res

        