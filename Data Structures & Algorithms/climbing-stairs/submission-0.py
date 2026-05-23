class Solution:
    def climbStairs(self, n: int) -> int:
        #we are given the choice between taking 1 step or 2 steps:

        one, two = 1,1 # the base case of num of ways to get to target value
        for i in range(n-1):    # n -1 since we start w/ step 1  
            temp = one
            one = one+ two
            two = temp    
        return one