class Solution:
    def rob(self, nums: List[int]) -> int:
         
        #amount of money cant rub adjacent houses reutrn max amt 
        #can either rob the current house or skip

      
        
        ret =0 
        '''
        memo ={} # MEMO = max containing this house 

        def dfs(curr, prevHouse,total):
            nonlocal ret
            if curr >= len(nums):
                ret = max(ret,total)
                return

            dfs(curr+1, prevHouse,total) #skip
            if curr-prevHouse >1 :
                dfs(curr+1,curr,total + nums[curr])# rob

        dfs(0,-2,0)
        return ret
        '''
        #TRY DP NHOW 
        if len(nums) ==1:
            return nums[0]

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        #0,2,3,3,4,1,0,
        #get max of arr expect prev 
        # [0,2,3,5,7,6,7 ] -> Max is 7
        for i in range(2,len(nums)):
            dp[i] = nums[i] + max(dp[0:i-1])
        return max(dp)
      