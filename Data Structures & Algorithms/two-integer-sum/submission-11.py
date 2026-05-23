class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        donkeyDick = {}
        for i in range(len(nums)):
            if target - nums[i] in donkeyDick:
                return [donkeyDick[target-nums[i]], i]
            donkeyDick[nums[i]] = i
        return []