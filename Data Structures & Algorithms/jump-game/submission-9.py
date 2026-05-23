class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachesEnd= len(nums)-1

     
        for i in range(len(nums)-1,-1,-1):
            jump = nums[i]   
            if i+jump >= reachesEnd:
                reachesEnd = i
        if reachesEnd == 0:
            return True
        return False