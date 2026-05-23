class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} # a hash map that will store our most frequent values 
        for num in nums:
            if num in freq_map:
                freq_map[num]= freq_map[num] + 1 #increments value // +=?
            else: #not in hashmap 
                freq_map[num] = 1
        #now hashmap is populated, return the top k lmnts
        return_array = []
        k_count = k
        dic = freq_map.items()
        

        while k_count>0:
            for keys in freq_map:
                if freq_map[keys] ==  max (freq_map.values()):
                    return_array.append(keys)
                    freq_map.pop(keys)
                    k_count -= 1
                    break

        return return_array

        

        