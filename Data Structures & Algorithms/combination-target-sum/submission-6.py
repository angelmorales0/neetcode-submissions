class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
       

        def dfs(index, arr, tot):
            if index >= len(nums) or tot > target:
                return
            if tot == target:
                print(1)
                ret.append(arr.copy())
                return 
            arr.append(nums[index])
            dfs(index,arr,tot + nums[index])
            arr.pop()
            dfs(index + 1,arr,tot)
        dfs(0,[],0)
        return ret
        