class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        ret = 0

        while l <= r < len(prices):
       
            if prices[r] - prices[l] >= 0:
                ret = max(ret, prices[r] - prices[l] )
                r +=1

            else: # we lose money
                l+=1 
        return ret 

