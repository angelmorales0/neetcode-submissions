class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 1
        ret = 1
        NS = set(nums)
        if not nums:
            return 0

        for num in NS:
            while num+maxLen in NS:
                maxLen +=1
                ret= max(ret, maxLen)
            maxLen = 1
        return ret
             
        
