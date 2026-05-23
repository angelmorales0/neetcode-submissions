class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #try the backtrack approach using memoization 
        dp = [float('inf')] * (amount+1) #gets our array initalized for DP, #inf is default val 
        dp[0] = 0 # because it takes 0 coins to get to 0, array houses min coins req
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    
                    temp = i-coin #because i is the amount
                    dp[i] 
                    dp[i] = min(dp[i], 1 + dp[temp]) #1 + since we are using a coin to get that value 

        if amount == 0:
            return 0
        if dp[amount] == float('inf'): #no valid coin combo found 
            return -1
        return dp[amount]
        