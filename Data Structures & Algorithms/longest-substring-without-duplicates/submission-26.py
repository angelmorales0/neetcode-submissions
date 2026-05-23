class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we have a contigous sequence of chars within a string -> so we cold use a sliding windi appraoch 
        
        #seen set ->
        #grow window while valid, -> when we get an invalid window shrink it until it is valid agian

        #loop through string with char 
            #see if char is in a set: if it is shrink the windows l pointer uintil we are valid again 
                #increment l pointer popping chars l points to off the set  until our current char is out of set 

            #add char to a set 
            # increment r pointer 
            #ret = max(r-l+1, ret)

        #test 

        #zxyzxyz 
    
        l =0
        seen = set()
        ret = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ret = max(ret, r-l+1)
        return ret