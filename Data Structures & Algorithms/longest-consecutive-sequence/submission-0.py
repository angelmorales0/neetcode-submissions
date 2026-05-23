class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NS = set(nums)
        maxLen = 0
       
        for num in NS:
            length = 1
            nem = num
            while (nem)-1 in NS:
                length += 1
                nem -=1
            maxLen = max(maxLen,length)
        return maxLen

        