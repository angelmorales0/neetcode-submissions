class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup_set = set()
        left_index = 0
        current_max = 0
        if len(s) == 0:
            return current_max
        if len(s) == 1:
            return current_max+1
    #opens the window to the rigth  
        for right_index in range(len(s)): 
            if s[right_index] in dup_set:
                while s[left_index] != s[right_index]:
                    dup_set.remove(s[left_index])
                    left_index += 1 #gets us to the repeated value
                    
                dup_set.remove(s[left_index])
                left_index += 1
                
            dup_set.add(s[right_index])
           
                #check current max 
            potential_max = 1+right_index - left_index
            current_max = max(current_max, potential_max)

        return current_max

     # Then shrink the window 


            
            

        