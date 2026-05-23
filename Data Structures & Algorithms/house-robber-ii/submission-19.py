class Solution:
    def rob(self, nums: List[int]) -> int:
        ret = [0,0]
        ret.extend(nums[1::])
        ret2 = [0,0]
        ret2.extend(nums[:len(nums)-1:])
        if len(nums) == 1:
            return nums[0]
        for i in range(2,len(ret)):
            ret[i] = max(ret[i-2] + ret[i],ret[i-1])
        for i in range(2,len(ret2)):
            ret2[i] = max(ret2[i-2] + ret2[i],ret2[i-1])
        
        
        print(ret,ret2)
        return max(ret[-1], ret2[-1])
            
        