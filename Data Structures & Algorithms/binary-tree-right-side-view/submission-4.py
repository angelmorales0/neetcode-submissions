# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append([root, 1])
        else:
            return []
        res = [[root.val, 1]]

        
        level = 1
        while q:
            node = q.pop()
            if node[0].left:
                q.appendleft([node[0].left, node[1] +1])
                res.append([node[0].left.val, node[1] +1])

            if node[0].right:
                q.appendleft([node[0].right, node[1] +1])
                res.append([node[0].right.val, node[1] +1])

        sets= set()
        ret = []

        for array_index in range (len(res)-1, -1, -1):
            if res[array_index][1] not in sets:
                ret.append(res[array_index][0])
                sets.add(res[array_index][1])
        ret.reverse()

        return ret