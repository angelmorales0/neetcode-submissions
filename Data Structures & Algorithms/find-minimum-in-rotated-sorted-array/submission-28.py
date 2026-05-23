class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) -1 # gets the indexs
        curr_min = nums[L]
        while L <= R:
            M = (L + R) // 2
            if nums[L] < nums[R]:
                curr_min = min(curr_min, nums[L]) # as array is sosrted 
                break
            if nums[M] < nums[R]:
                curr_min = min(curr_min, nums[M])
                R = M - 1
            if nums[M] >= nums[R]:# if nums M > R Array is unsorted 
                curr_min = min(curr_min, nums[R])
                L = M + 1
        return curr_min