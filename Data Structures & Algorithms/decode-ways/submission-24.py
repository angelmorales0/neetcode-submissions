class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s):1 } #defualt base case
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 #you cant decode it so it KILLS the tree
                #dp[i] = max ways to decode starting at I as the index 
            else:
                dp[i] = dp[i+1] #then its a subprob of the next SINCE we can take it
            #if i + 2 is possible 
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i+2]
        print(dp)
        return dp[0]


