class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #retry using a hashmap 
       if len(s) != len(t):
        return False

       s_hashmap = {}
       t_hashmap = {}

       for letter in s:
        s_hashmap[letter]= s_hashmap.get(letter,0) + 1
       for letter2 in t:
        t_hashmap[letter2] = t_hashmap.get(letter2,0) +1

       t_keys = list(t_hashmap.keys())
       s_keys = list(s_hashmap.keys())

       t_keys.sort()
       s_keys.sort()
       print (t_keys)
       print (s_keys)
        
       for index in range(len(t_keys)):
            if t_keys[index] != s_keys[index]:
                return False

       for key in s_hashmap:
        if s_hashmap[key] != t_hashmap[key]:
            return False
       return True
       # todo check if keys are equal?     