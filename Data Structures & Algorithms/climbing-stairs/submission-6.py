class Solution:
    def climbStairs(self, n: int) -> int:
        #n = steps to reach top of staircase can either climb 1 OR 2 aty a time. return all ways to get to top

        #BF BACKTRACKING APPROACH 
        
        #get all possible inputs of 1 /2 to get to step N and return count 

        #try to memoize itr
        """
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

            #NEED TO GET EVERY SINGLE UNIQUE WAY 
        """
        
        dp = [0]*(n+2)
        dp[0] = 1
        for i in range(n):
            if dp[i] >=1 :# it is possible
                dp[i+1] +=dp[i]
                #1->2->3
                #2->3
                #1->3
                #[1,1,2,3]
                dp[i+2] +=dp[i]
        return dp[n] 
