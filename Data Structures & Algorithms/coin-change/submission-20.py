class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins is an int array 
        '''
        given an integer array of inputs and a target
        need to query them 
        and return the fewest amount of coins that make up the exact amount
        '''
        #no not sorted


        #while we can decreae the amount we can continues 
        dp = [-1]*(amount+1)

        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        for coin in coins:
            if coin in range(len(dp)):
                dp[coin] = 1
        
        for i in range(1, amount+1):
            for coin in coins:
                amountNeeded = i - coin
                if amountNeeded in range(len(dp)) and dp[amountNeeded] != -1:
                    if dp[i] != -1:
                        dp[i] = min(dp[i], 1+ dp[amountNeeded])
                    else:
                        dp[i] = 1 + dp[amountNeeded]
        print(dp)
  
                
        return dp[amount]
