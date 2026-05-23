class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            ret = [float('inf')]*(amount+1)
            ret[0] = 0
            #[0, inf, inf]

            for amt in range(1, amount+1):
                for coinVal in coins:
                    needed_coins = amt - coinVal
                    if needed_coins <0:
                        continue
                    ret[amt] = min(ret[amt], 1 + ret[needed_coins])

            if ret[amount] == float('inf'):
                return -1
            return ret[amount]


           