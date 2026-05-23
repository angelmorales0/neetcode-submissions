class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        #ex: nums = [1,2] dp = [todo, 1]
        #what should I return if empty?
        dp[-1] = 1
 

        for i in range(len(dp)-2,-1,-1):
            #if num is < nums[i+1] dp[i] = 1 + dp[i+1] dp[i]
            # = max length of increasing subArray INCLUDEING that VALUE
            best_dp =[-1,-1] #index, dp val

            for j in range(i+1,len(nums),1):
                if nums[i] < nums[j] and dp[j] > best_dp[1]:
                    best_dp[0] = j
                    best_dp[1] = dp[j]
    
            if best_dp[0] != -1:
                dp[i] = 1 + best_dp[1]
            else:
                dp[i] = 1
            
        return max(dp)
