class Solution:
    def climbStairs(self, n: int) -> int:
        #n = steps to reach top of staircase can either climb 1 OR 2 aty a time. return all ways to get to top

        #BF BACKTRACKING APPROACH 
        
        #get all possible inputs of 1 /2 to get to step N and return count 
        count = 0
        def backtrack(steps_left):
            nonlocal count
            if steps_left < 0:
                return 
            if steps_left == 0:
                count +=1
                return 
            backtrack(steps_left - 1)
            backtrack(steps_left - 2)
        backtrack(n)
        return count 
