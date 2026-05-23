class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

#Solution, levelOrder, TreeNode
class Solution:
    def levelOrder(self, root):
        q = deque()
        ret = []

        if root:
            q.append(root)
        #need q append?
        while q:
            nodes_on_level = len(q)
            level = []
            for _ in range(nodes_on_level):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(level)
        return ret 