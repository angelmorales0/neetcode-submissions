class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []

        #ordering doesnt matter i a subset 
        def dfs(index):
            if index >= len(nums):
                ret.append(subset.copy())
                return 
            #add type 
            subset.append(nums[index])
            dfs(index+1)

            subset.pop()
            dfs(index + 1)
        dfs(0)
        return ret