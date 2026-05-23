class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # left pointer, right pointer = 0, len(nums) -1
        # ret = -1
        # middle = right pointer + left pointer // 2

        #while L < R:
            # middle = right pointer + left pointer // 2


            #if target < middle value:
                #must be in left
            #elif target > middle value:
                #must be in right 
            #else:
                #return middle

        l = 0
        r = len(nums)-1
        ret = -1

        while l<=r:
            middle = (r+l) //2
            if target == nums[middle]:
                return middle 

            if target < nums[middle]:
                r = middle-1
            elif target > nums[middle]:
                l = middle+1
           
        return ret
        

