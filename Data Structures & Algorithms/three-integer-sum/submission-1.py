class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        hash_set = set()

        for i in range (len(nums)-2):
            for j in range (i+1,len(nums)-1):
                for k in range (j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        S_L = [nums[i], nums[j], nums[k]]
                        S_L.sort()
                        if tuple(S_L) not in hash_set:
                            return_array.append(S_L)
                        hash_set.add(tuple(S_L))
                        
        return return_array
