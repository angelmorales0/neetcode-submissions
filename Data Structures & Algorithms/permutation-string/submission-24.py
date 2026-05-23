class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, R = 0, 0
        s1_map = {}
        s2_map = {}

        if len(s2) < len(s1):
            return False    
        
        # Build the frequency map for s1
        for letter in s1:
            s1_map[letter] = s1_map.get(letter, 0) + 1 
        
        # Initial window size of s1 in s2
        for i in range(len(s1)):
            s2_map[s2[R]] = s2_map.get(s2[R], 0) + 1 
            R += 1  # sets window size  
        R -= 1
        
        while R < len(s2):
            if s2_map == s1_map:
                return True
            
            s2_map[s2[L]] = s2_map.get(s2[L], 0) - 1 
            if s2_map[s2[L]] == 0:
                s2_map.pop(s2[L])
            L += 1
            
            R += 1
            if R < len(s2):
                s2_map[s2[R]] = s2_map.get(s2[R], 0) + 1 
        
        return False
        