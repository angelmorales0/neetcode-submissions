class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachesEnd=[]
        end = len(nums)-1
     
        for i in range(len(nums)-1,-1,-1):
            for jump in range(nums[i]+1):
                if i+jump == end:
                    reachesEnd.append(i)
                elif i+jump in reachesEnd:
                    next_index = reachesEnd.index(i+jump)
                    reachesEnd[next_index] = i 
        print(reachesEnd)
        if 0 in reachesEnd:
            return True
        return False