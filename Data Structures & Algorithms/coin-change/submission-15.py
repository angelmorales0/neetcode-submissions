class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Return the fewest number of coins that you need to make up the exact
        

        #approaches 
        #1. Greedy? Would this work -> No [1,5,6,10] for 12. -> 3 not 2 
        # DP where one input is based off another since this is a summation type of problem
            #have an amount array where each index contains the min amnt to get to the index and your return that index?
            
            #[1,5,10] -> 
            #[]
            # 0, 1, 2, 
            #or a decision tree that terminates when we exceed amnt? 
            # 1->1-> 1-> .. 
            #10 -> 5 -> 1 -> 1-> Honestly feel more comfy with the decision tree
            # I think dp approach would be better 

            ret = [-1]*(amount+1)

            if amount ==0:
                return 0
            #Input: coins = [1,5], amount = 6
            #[-1,-1,-1,-1,-1,-1, -1]

            #then filli nm out coin vals 
            minCoin = -1
            for coin in coins: # -> O(n)
                if minCoin == -1:
                    minCoin = coin #gets the minimum Coin
                if coin < len(ret):
                    ret[coin] = 1
            
          
            for i in range(minCoin+1,amount+1,1): # goes till amount from 1+ smallest index
                minCoinsNeeded = float('inf')
                if i in coins:
                    continue
                for coin in coins:
                    coins_prev_needed = i-coin

                    if coins_prev_needed < 0 or ret[coins_prev_needed] == -1:
                        continue
                    minCoinsNeeded = min (minCoinsNeeded, 1+ret[coins_prev_needed])

                if minCoinsNeeded != float('inf'):
                    ret[i]= minCoinsNeeded 
            return ret[amount]
                  
                #index = 1+ min (index - coin amount if coin amount != -1, else = -1) since no way to advance 
                #newtarget = index - coin amount

            #return ret[amount}]


           