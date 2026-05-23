class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) -1 # gets the indexs
        curr_min = float("inf")
        while start <= end:

            if nums[start] < nums[end]:
                curr_min = min(curr_min, nums[start])
                break

            M = ( start + end )//2
            curr_min = min(curr_min, nums[M])

           

            if nums[M] < nums[end]: #Min val must be on M's Left 
                end = M -1
            if nums[M] >= nums[end]: # min val must be on M's Right
                start = M +1
        return curr_min

