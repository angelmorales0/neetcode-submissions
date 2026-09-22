class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input: an integer array of prices containing the price on the ith day 
            you can buy and sell, cant buy one day after a sell (1 day cooldown)can only own 1 

        need to find the maximum profit combination following these rules 
        output: maximum profit

        Since we are trying to find a max/min optimal value we can either do it greedy or with dp 

        Greedy = the best choice now is the best choice always in this case it is not so dp is more viable 

        """

        dp = {}# sell map max profit
        holding = False

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

        return dfs(0,False)





        
        """
        cooldown = cant do anything (post sell) 
        sell = must be boldng 
        buying = must NOT be holding 
        State = holding or not holding
        
        options are do nothing, buy, or sell  at each step
        """
            
            