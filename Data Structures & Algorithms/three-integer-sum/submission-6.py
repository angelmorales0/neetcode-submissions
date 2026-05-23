class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #ensures we dont get dupes thru sorted array!!
                continue

            L,R = i+1, len(nums)-1 #initializes L and R pointers 
            while L < R:
                nums_tot = nums[i] + nums[L] + nums[R]
                if nums_tot < 0: # we are below target so tot must get bigger
                    L += 1
                elif nums_tot > 0:# we are above target so tot must get smaller 
                    R -= 1 
                else:
                    return_array.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        return return_array