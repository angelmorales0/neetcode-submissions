class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        BF -> Double for loop o(n)^2

        1->2 -> 3 -> 7 : 2
        Based off the end tho?
        3 -> 7 
        if == ignore 
        if < then add 1 to it 
        1 2 3 4 2 4 5
                  3 2 4 5
        keep a value < max seeen AND not in set 
        [9,1,4,2,3,7 10,11,12,13]
        Keep in set o(n) space
        [     3 2 2 1]
        Go @ end 
       [0,3,1,3,2,1]
       o(n^2) time and o(n^2) space
       2d ARR [ num :len list including it , sorted]
       7:1
       for all vals greater than current increment count by 1 
       1: 1 2:2 3:3 7:4 9:1
       return max of subsequences 
        3:3
        2:2
        1:1

        """
    
        dp = [1]*len(nums) #default val

        """
        Q How do you account for adding the value to differen tpahts?
        """ 
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]: # we are decreasing so we can update it 
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

            
