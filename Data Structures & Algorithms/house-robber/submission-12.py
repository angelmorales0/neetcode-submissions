class Solution:
    def rob(self, nums: List[int]) -> int:
         
        #amount of money cant rub adjacent houses reutrn max amt 
        #can either rob the current house or skip

      
        
        ret =0 
     
        dp = [0]*len(nums)
        dp[0] = nums[0]

        #[1,1,3,3]
        #[1,1,0,0]
        for i in range(1,len(nums)): 
            dp[i] = max( dp[i-1], nums[i] + dp[i-2])
        return dp[-1]
      