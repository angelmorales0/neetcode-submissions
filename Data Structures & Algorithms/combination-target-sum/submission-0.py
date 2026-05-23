class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        curr = []
        hashset = set()
        def dfs(index):
            tot = 0
            for num in curr:
                tot += num
            if tot == target:
                if tuple(curr.copy())in hashset:
                    return
               
                ret.append(curr.copy())
                hashset.add(tuple(curr.copy()))
                return
            if index >= len(nums) or tot > target:
                return

            #To include current num

            curr.append(nums[index])
            dfs(index)

            curr.pop()
            index += 1
            dfs(index)

            dfs(index)
        dfs(0)
        return ret

        