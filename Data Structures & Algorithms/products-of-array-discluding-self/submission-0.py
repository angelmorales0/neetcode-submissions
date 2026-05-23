class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        value_map = {}
        to_append = 1
        for index in range (len(nums)):
            value_map[index] = nums[index]
        #populates the hash map, key = index and value = values 
        return_array = []
        for key_ignore in value_map:
            for key in value_map:
                if key == key_ignore:
                    to_append += 0
                else:
                    to_append = to_append*value_map[key]
            return_array.append(to_append)
            to_append = 1
        return return_array

