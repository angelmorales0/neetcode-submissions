class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []

        #make the key a words letters in alphabetical order 
        #add the key to a map 
        #return all keys 
        
        #map = {}
        #get letters 
        #add letters to map 
        #extract it from map 
        #reutn extracted words 

        mapp = {}
        curr = ""
        for word in strs:
            curr = ""
            for ltr in word:
                curr += ltr
            key = "".join(sorted(curr))
            if key not in mapp:
                mapp[key] = []
            mapp[key].append(curr) 
        return mapp.values()
           

        