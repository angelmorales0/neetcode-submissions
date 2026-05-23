class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0,len(nums) -1
        while L <= R:
        
            M =  int((L + R )//2)
            if nums[M] >= target: # its on the left side
                R= M-1 
            if nums[M] < target:
            #its on right 
                L = M+1
            if nums[M] == target:
                return M
                #num not found 
        return -1

        