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

            doNothing = dfs(i+1, holding)

            if not holding:
                buy = dfs(i+1, not holding) - prices[i]
                dp[(i,holding)] = max(buy,doNothing)
            
            if holding:
                sell = dfs(i+2, not holding ) + prices[i]
                dp[(i,holding)] = max(sell,doNothing)

            return dp[(i,holding)]
            

        return dfs(0,False)
        #dp (i,holding) is the max profit from the end to here 
     
            
            