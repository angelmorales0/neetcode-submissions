class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        goal = len(nums)-1
        dp[goal] = 0 #as it is goal 
        distance = 0
        for i in range(goal-1,-1,-1):
            if i + nums[i]>= goal:#if index+jump is over or at goal
                dp[i] = 1
            else:
            
                possible = nums[i]
                minjumps = float('inf')
                while possible >= 1:
                    minjumps = min(minjumps,dp[i+possible])
                    possible -= 1
                dp[i] = 1 + minjumps # will probably need to repeat while num >= 1


        print(dp)
        return dp[0]
            # if goal is within reach, DP = 1 as it takes one jump
            #otherwise, dp[i] = dp of the next jump

        