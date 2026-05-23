class Solution:
    def climbStairs(self, n: int) -> int:
        #we are given the choice between taking 1 step or 2 steps:
        one, two = 1,1 
        ret = 0
        if n == 1:
            return 1

        for i in range(n-1, 0, -1):
            ret = one + two
            temp = one
            one = ret
            two = temp
        return ret