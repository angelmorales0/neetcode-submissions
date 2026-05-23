class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = max(nums)
        curr_max = 1
        curr_min =1

        for num in nums:
            temp = curr_max
            curr_max =  max (num,curr_min * num,curr_max * num)
            curr_min = min(num,curr_min * num, temp*num)
        
            if num == 0:
                #num == 0 so we need to restrart our sub array
                curr_max = 1
                curr_min = 1
                continue #since you cant add 
            ret = max (ret, curr_max,curr_min,num)
      
        return ret