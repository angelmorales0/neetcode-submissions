class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #try the backtrack approach using memoization 
        memo = {}
        

        def dfs(total): # to get every possible permutation 
            if total in memo:
                return memo[total]

            if total == 0:
                return 0 
                
            if total < 0:
                return float('inf')
            #memo is the min amount of coins needed @ that step 
            minCoins = float('inf')

            for coin in coins :
                numCoins = 1 + dfs(total - coin)
                if numCoins != float('inf'):
                    minCoins = min(minCoins, numCoins)
            memo[total] = minCoins
            return memo[total]

            


        dfs(amount)
        ret = float('inf')
        if amount == 0:
            return 0
        if memo[amount] == float('inf') :
            return -1 #as it is impossible
        
        return memo[amount]

        

