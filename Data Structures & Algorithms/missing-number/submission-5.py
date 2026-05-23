class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        nums.sort()
        for i in range((len(nums))):
            if i != nums[i]:
                return i
        return len(nums)