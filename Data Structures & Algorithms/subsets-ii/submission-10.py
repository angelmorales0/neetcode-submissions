class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        cur = []

        def backtrack(i):
            if i >= len(nums):
                ret.append(cur.copy())
                return


            cur.append(nums[i])
            backtrack(i+1) #all subsets inlcuding current num 
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+= 1
            backtrack(i+1)


        backtrack(0)
        return ret

