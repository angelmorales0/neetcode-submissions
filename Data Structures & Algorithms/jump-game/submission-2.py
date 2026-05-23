class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        jumpCount = 0
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= goal:# we can move our goal post back
                goal = i
                #as it is jumpable 
        if goal == 0:
            return True
        return False
                
           
        return True 
        