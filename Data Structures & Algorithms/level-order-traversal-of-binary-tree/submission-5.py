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
            res.append([curr[0].val, curr[1]])
            if curr[0].left:
                q.appendleft([curr[0].left, curr[1]+1]) 
            if curr[0].right:
                q.appendleft([curr[0].right, curr[1]+1])

        for array in res:
            if array[1]-1 in range(len(ret)):
                print(array[1]-1, 'sub')
                ret[array[1]-1].append(array[0])
            else:
                ret.append([array[0]])
 

        return ret

        