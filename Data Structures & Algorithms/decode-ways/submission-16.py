class Solution:
    def numDecodings(self, s: str) -> int:
        #decision tree
        
        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0
            ret = dfs(i+1)

            if (i+1 <len(s) and s[i] == "1" or i+1 <len(s )and s[i] == "2" and int(s[i+1]) <= 6):
                ret += dfs(i+2)
            dp[i] = ret

            return ret


        return dfs(0)
