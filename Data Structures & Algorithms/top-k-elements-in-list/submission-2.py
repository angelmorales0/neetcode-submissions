class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} # a hash map that will store our most frequent values 
        return_array = []
        k_num = k
        for num in nums:
            freq_map[num]= freq_map.get(num,0) + 1 #increments value 
          
        #now we have a hash_map with our values however the key is what we want, not the value
        #so we will create an array where the 
        count_array = [ [] for i in range(len(nums) + 1)] # now we have a return array 
        #wehre the key is the amount of times the value has occured  and the value is the values that occured x times


        for number, occurances in freq_map.items():
            count_array[occurances].append(number)

        
        for index in range(len(nums),0,-1): #negative for loop that starts at the end and goes to start 
            for i in range (len(count_array[index])):
                return_array.append(count_array[index][i])
                k_num -= 1
                if k_num <= 0:
                    return return_array
        return return_array

        

        