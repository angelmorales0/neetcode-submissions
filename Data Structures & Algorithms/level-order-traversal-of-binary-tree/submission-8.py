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
            q.append([root, 0])
        #need q append?
        while q:
            node,level = q.popleft()

            if level < len(ret):
                ret[level].append(node.val)
            else:
                ret.append([node.val])

            if node.left:
                q.append([node.left,level+1])
            if node.right:
                q.append([node.right,level+1])
        return ret 