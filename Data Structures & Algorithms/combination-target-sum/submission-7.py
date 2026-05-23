class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       # 3FIND ALL UNIQUE COMBOS WHERE NUMS SUM TO TARGET
       #combos are the same if the chosen frequency is the same of nums 
       #since we can resue nums ^ 

       #idea -> Find all subsets, see if they sum to target add it to ret 

        ret = []
        memo = set()

        def alr_seen(subset):
            freq = {}
            for num in subset:
                freq[num] = freq.get(num,0) + 1 
            if tuple(sorted(freq.items())) in memo:
                return True
            return False

        def backtrack(curr):
            tot = sum(curr)
            if tot > target:
                return
            if alr_seen(curr):
                return
            if tot == target:
                ret.append(curr.copy())
                freq = {}
                for num in curr:
                    freq[num] = freq.get(num,0) + 1 #gets us num:count
                memo.add(tuple(sorted(freq.items())))

            for num in nums:
                curr.append(num)
                backtrack(curr)
                curr.pop()

        backtrack([])
        return ret


        