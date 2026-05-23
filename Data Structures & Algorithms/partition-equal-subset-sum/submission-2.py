class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #first approach is back tracking? 
        """
        Find all possible subsets which for n elements is 2^n work? since we can include or exlcue every subset?
        then go through all sub sets and see what matches O(n^2)

        O(2^n)
        """
        subsets = []

        def dfs(index, subset):
            if index >= len(nums):
                subsets.append(subset.copy())
                return
            dfs(index+1, subset)
            subset.append(nums[index])
            dfs(index+1, subset)
            subset.pop()
        dfs(0,[])

        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2  
        for subset in subsets:
            if sum(subset) == target:
                return True
        return False