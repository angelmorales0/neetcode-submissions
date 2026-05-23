class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = 0
        prev = 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        curr = 1

        for i in range(len(nums)):
            negPresent = False

            curr = curr * nums[i]
            ret = max(ret, curr)

            if nums[i] == 0:
                #we also reset
                curr = 1
            if curr < prev:
                #see if neg is present in rest
                for j in range( i+1, len(nums)):
                    if nums[j] < 0:
                        negPresent = True
                    #makes a neg present if 
                if not negPresent:
                    curr = 1 # restart array 

            prev = curr
        return ret
            
            
        