class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for index in range (len(nums)):
            need = target - nums[index]
            if need in mapp:
                return [mapp.get(need),index]
            mapp[nums[index]] = index
                
