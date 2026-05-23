# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #given Binary trees, NOT binary search trees

        #run bfs on root tree intil we find same root, then q on both and see if we match,
        # if we do great, if not put it in the bag
        def isSameTree(root,subRoot):
            q1 = deque()
            q2 = deque()
            q1.append(root)
            q2.append(subRoot)

            while q1 and q2:
                n1 = q1.popleft()
                n2 = q2.popleft()
                print(n1.val,n2.val)
                if n1.val != n2.val:
                    return False

                if n1.left:
                    q1.append(n1.left)
                if n1.right:
                    q1.append(n1.right)
                if n2.left:
                    q2.append(n2.left)
                if n2.right:
                    q2.append(n2.right)
            if q1 or q2:
                return False
            return True

        find_q = deque()
        if root:
            find_q.append(root) 
        while find_q:
            node = find_q.popleft()

            if node.val == subRoot.val:
                if isSameTree(node,subRoot):
                    return True
            if node.left:
                find_q.append(node.left)
            if node.right:
                find_q.append(node.right)
        return False
        

        