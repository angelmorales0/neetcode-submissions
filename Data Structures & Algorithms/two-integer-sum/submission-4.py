class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I and J must be two different indices and their values 
        #witihin the array must add up to target
        L = 0
        R = 1

        while L <= len(nums)-2:
            while R <= len(nums)-1:
                 if nums[L] + nums[R] == target:
                    return [L,R]
                 R += 1
            L += 1
            R = L +1
            
