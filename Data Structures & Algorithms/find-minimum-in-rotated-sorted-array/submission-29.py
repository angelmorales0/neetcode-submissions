class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 -> 4 -> 5 -> 6 -> 1 -> 2                    
        #                      L   R   

        #have our L and R pointers 

        #shift R back until the value at R is > value at L 
            #Now we knwo the values between L and R are sorted 
            #if  val is within this just run b-search 
            #else value must have been seen by r so we just check to retu

        l, r = 0, len(nums)-1
        ret = nums[l]
        while l < r:
            m = (l + r)//2
            if nums[m] >= nums[l]: # we are sorted and are not at our minimum tho l could be min
                l = m+1
                ret = min (ret, nums[l])
            elif nums[m] < nums[l]: # we are not sorted and it must be in this
                r = m-1
                while l < m:
                    if nums[m-1] > nums[m]:
                        return nums[m]
                    m -=1
        return ret
                

