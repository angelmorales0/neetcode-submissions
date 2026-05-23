class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max=0
        for buy_index in range (0, len(prices)):
            for sell_index in range (buy_index,len(prices)):

             if prices[sell_index] - prices[buy_index] > current_max:
                 current_max = prices[sell_index] - prices[buy_index]

        return (current_max)