class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]* (len(s)+1)
        dp[-1] = True

        for i in range(len(dp)-2,-1,-1):
            for j in range(i+1,len(dp)):
                if s[i:j] in wordDict and dp[j]:
                    dp[i] = True
        return dp[0]
                    
