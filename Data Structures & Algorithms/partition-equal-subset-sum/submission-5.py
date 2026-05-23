class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #first approach is back tracking? 
        """
        Find all possible subsets which for n elements is 2^n work? since we can include or exlcue every subset?
        then go through all sub sets and see what matches O(n^2)

        O(2^n)
        """
        subsets = []
        """
        I shouldnt need to calculate every subset I just need one good one 

        """
       
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2  


        def dfs(index, tot):
            print(tot)
            if tot == target:
                return True
            if tot > target or index >= len(nums):
                return False
            return dfs(index+1,tot) or dfs(index+1, tot + nums[index])

        return dfs(0,0)