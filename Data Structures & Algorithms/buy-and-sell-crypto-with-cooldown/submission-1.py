class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}# sell map max profit

        """
        
        options are do nothing + (buy OR  sell) at each step
        """
        def dfs(i, holding): # returns the value?
            if i >= len(prices):
                return 0

            if (i,holding) in dp:
                return dp[ (i,holding) ]

            holdPosition = dfs(i+1, holding)


            if not holding:
                buy = dfs(i+1, not holding) - prices[i]
                dp[(i,holding)] = max(buy,holdPosition)
            
            if holding:
                sell = dfs(i+2, not holding ) + prices[i]
                dp[(i,holding)] = max(sell,holdPosition)
            
            return dp[(i,holding)]
        print(dp)
        return dfs(0,False)

     
            
            