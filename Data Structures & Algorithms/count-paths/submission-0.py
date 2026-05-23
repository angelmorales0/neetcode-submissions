class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #2 options go down and go right 
        dp = [[0] *(n+1) for _ in range(m+1)] #dp is expanded to incldue 0's
        dp[m-1][n-1] = 1 #btm rihgt you have 1 way of getting there 
    
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r == m-1 and c == n-1:
                    continue # since we dont want to change the goal
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        print(dp)
        return dp[0][0]