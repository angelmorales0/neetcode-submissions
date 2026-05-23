class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        final = len(cost)
        mincost = float('inf')
        arr = []
        ret = []
    

        def dfs(i):
            #cost of ith index = cost of prev sum 
            if i == final:
                print(1)
                ret.append(arr.copy())# 
                return #we are DONE 
            if i> final:
                return

            arr.append(cost[i]) # adds current cost 

            dfs(i+1)
            dfs(i+2)

            arr.pop()

        dfs(0)
        dfs(1)

        for array in ret:
            temp = 0
            for value in array:
                temp += value
            mincost = min(mincost, temp)

        return mincost
        