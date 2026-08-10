class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        racecar
        
        carrace
        """
     
        return Counter(s) == Counter(t)