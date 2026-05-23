class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                arr.append(cur.copy())
                return

            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack()
                    cur.pop()
        backtrack()
        return arr
                