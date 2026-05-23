class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #return all combos of 3 where nums[val] = 0

        #first idea is to use a backtracking approach 
        #but this is 2 ptrs so ima try that firs tbut backtracking lowkey seems easier?

        #sorting = we only grow by going right,
        #leftmost value is min if not  < 0 return 
        #how to pick which value to pop off

        #start with most neg value, and add all rest of values, 
        # if greater than 0 then see if a value exists such that if you pop it off you get 0 else pick the closest value to 0 
        #fuck it back traacking 

        ret = []
        nums.sort()

        for i in range (len(nums)):
            if i != 0 and nums[i-1] == nums[i]: #this is our A value
                continue 
            #now we run two sum and find out our other 2 
            l = i+1
            r = len(nums)-1

            while l <r:
                value =  nums[i] + nums[l] +nums[r]
                if value == 0:
                    ret.append([nums[i], nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
                elif value > 0:
                    #we need to go down so 
                    r-=1
                else:
                    l+=1
                   
        return ret
                
