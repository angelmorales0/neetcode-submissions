class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #int K and a string 
        #can replace up to K characters
        #rturn longest strings containing only one char 

        l =0
        r=0
        ret = 0
        letters = {}
        letters[s[0]] = 1

        def isValid(length):
            maxLetter = max(letters.values(),default=0)
            print(maxLetter)
            if length <= maxLetter + k:
                return True
            return False

        while r < len(s):
  
            while isValid(r-l+1):
                if r >= len(s):
                    return ret
                ret = max(ret, r-l+1)
                r+=1
                if r < len(s):
                    letters[s[r]] = letters.get(s[r],0)+1
           
            
            while l<r and not isValid(r-l+1):
                letters[s[l]] -=1
                l+=1

  
        return ret
            

        #if increasing r means we are still valid do it 
            #remove K's if necessary
        #else
            #increase L until we are valid again 
            #if L changes character we re calc is valid under new character 