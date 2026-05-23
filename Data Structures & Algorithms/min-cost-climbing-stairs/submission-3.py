class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-2, -1, -1):

            
            if i-1 >= 0:
                cost[i-1] = min(cost[i-1] + cost[i], cost[i-1] + cost[i+1])
        return min(cost[0],cost[1])
        