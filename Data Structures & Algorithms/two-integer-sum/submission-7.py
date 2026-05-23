class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1,-1,-1):
            new = target - nums[i]
            sub = nums[0:i]
            if new in sub:
                for j in range(len(sub)):
                    if sub[j] == new:
                        return [j, i]
        