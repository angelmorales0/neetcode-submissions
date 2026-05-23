class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = float('-inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            ret = max(ret, total)
            if total < 0:
                #reset array 
                total = 0
        return ret
            
        