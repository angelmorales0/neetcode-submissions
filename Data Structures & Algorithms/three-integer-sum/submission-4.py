class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        hash_set = set()
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            L = i+1
            R = len(nums)-1
            while L < R:
                if nums[i] + nums[L] + nums[R] > 0: #we must shrink
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < 0: # we must goew
                    L += 1
                else: 
                    return_array.append([nums[i], nums[L], nums[R]])
                    L +=1
                    while nums[L] == nums[L-1] and L < R:
                        L +=1
        return return_array