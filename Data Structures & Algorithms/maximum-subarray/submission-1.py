class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        ret = float('-inf')

        for i in range(len(nums)):
            #we need to go through and if curr beocmes neg reset curr
            curr += nums[i]
            ret = max(ret,curr)
            if curr <0:
                curr=0
        return ret