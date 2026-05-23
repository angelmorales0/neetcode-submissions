class Solution:
    def rob(self, nums: List[int]) -> int:
        final = len(nums)

        nums[final-1]
        nums[final-2] 
        maxnum = 0
        #stay the same
        for i in range(final-3, -1, -1):
            if i+3 < final:
                nums[i] = nums[i] + max(nums[i+2],nums[i+3] )
            else:
                nums[i] = nums[i] + nums[i+2]
        print(nums)

        for num in nums:
            maxnum = max(maxnum, num)
        return maxnum



