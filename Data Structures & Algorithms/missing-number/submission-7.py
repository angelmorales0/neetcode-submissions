class Solution:
    def missingNumber(self, nums: List[int]) -> int:   
        ret = len(nums)
        for i in range((len(nums))):
            ret ^= i ^nums[i]
        return  ret
