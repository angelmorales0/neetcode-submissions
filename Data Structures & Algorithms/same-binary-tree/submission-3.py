# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque() 
        #want to solve this iteratviely to not lose track of ze call stack
        if p:
            q1.append(p)
        if q:
            q2.append(q)
        while q1 and q2:

            n1 = q1.popleft()
            n2 = q2.popleft()
            

            if not n1 and not n2:
                
                continue

            if not n1 or not n2 or n1.val != n2.val:
                return False

        
            q1.append(n1.left)
            q1.append(n1.right)
            q2.append(n2.left)
            q2.append(n2.right)

        if q1 or q2: #mismatch node a count
            return False
        print(q1,q2)
        return True
        