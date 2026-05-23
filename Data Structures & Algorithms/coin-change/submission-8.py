class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #try the backtrack approach using memoization
        memo = { }
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        def dfs(total):
            if total in memo:
                return memo[total]
            if total == 0:
                return 0
                #do sum
            if total <= 0:
                return float('inf')
            #if total is greater than 0 we simplify the problem 
            minCoins = float('inf')

            for coin in coins:
                currCoins =  1 + dfs(total-coin)
                if currCoins != float('inf'):
                    minCoins = min(minCoins, currCoins)
            print(total, currCoins)
            
            memo[total] = minCoins

            return memo[total]

        dfs(amount)
        ret = float('inf')
        if amount == 0:
            return 0
        if memo[amount] == float('inf') :
            return -1 #as it is impossible
        
        return memo[amount]
