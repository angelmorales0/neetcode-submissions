class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtrack(curr,i):
            tot = sum(curr)
    
            if tot > target or i >= len(nums):
                return
            if tot == target:
                ret.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(curr,i) # include keep going w/ repeat
            curr.pop()
            backtrack(curr,i+1) #dont include
        backtrack([],0)
        return ret


        
        