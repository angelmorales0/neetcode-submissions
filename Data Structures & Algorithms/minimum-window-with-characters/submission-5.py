class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #sliding window approach since itg is contigous 

        #grow the window WHILE we are invalid until the end 
        #then SHRINK the window while we are valid  to get to minimum 
        #valid ==  t count is contained in s count: 

        #iterate thru T and count p vals 

        #loop through s with r and l pointers for our window 
        #valid = True 
              
        #for r in range(len(s))
            #while valid 
                #for val in t:
                    #if val in sMap is equal to val in tMap for ALL vals:
                #ret = min(ret,curr strnig)
                #l+=1
                #valid = isValid()
            #add s[r] to smap 

        def isValid():
            for char in t:
                if char not in sMap or tMap[char] > sMap[char]:
                    return False
            return True
        sMap = {}
        tMap = {}
        l=0
        for char in t:
            tMap[char] = tMap.get(char,0) + 1
        ret = ""

        for r in range(len(s)+1):
            valid = isValid()
            while valid:
                #shrink the window 
                if not ret:
                    ret = s[l:r]
                if (r-l <= len(ret)):
                    ret = s[l:r]
                sMap[s[l]] -=1
                l+=1

                if not isValid():
                    break
            if r < len(s):
                sMap[s[r]] = sMap.get(s[r],0) + 1
        return ret



    