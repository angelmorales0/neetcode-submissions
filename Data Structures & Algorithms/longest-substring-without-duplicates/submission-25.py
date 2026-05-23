class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup_set = set()
        left_pointer = 0
        current_max = 0
        for right_pointer in range (len(s)):

            if s[right_pointer] in dup_set: #window shrinking conditions  
                while s[left_pointer] != s[right_pointer]:
                    dup_set.remove(s[left_pointer])
                    left_pointer += 1
                dup_set.remove(s[left_pointer])
                left_pointer += 1
            
            dup_set.add(s[right_pointer]) # window growing conditions 
            potential_max = 1 + right_pointer - left_pointer
            current_max = max(current_max, potential_max)
        return current_max


            
            

        