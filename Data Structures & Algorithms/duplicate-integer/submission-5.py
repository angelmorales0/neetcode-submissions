class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # if value appears more than once return True, else False

    # sett = set()

    #loop through the array
        #if value in set
            #return False 
        # add value to the set
    #return True 

        sett = set()

        for num in nums:
            if num in sett:
                return True
            sett.add(num)
        return False




         