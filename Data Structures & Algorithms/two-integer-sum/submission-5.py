class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index in range (len(nums)):
            if target - nums[index] in hash_map: #in checks if key exists 
                return hash_map[target - nums[index]], index
            hash_map[nums[index]] = index #number is the key, index is the value 
            

            
