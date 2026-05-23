class Solution:
    def countSubstrings(self, s: str) -> int:
        sett = set()
        count = 0
        curr = ""
        for i in range(len(s)):
        #default add as one character is substrin 
        #then we must check for palindromes around this character
            l = i
            r = i
            while l>=0 and r< len(s) and  s[l] == s[r]:
                curr = s[l:r+1]
                if curr == curr[len(s)-1::-1]:
                    sett.add( (i, curr) )# adds the cur sub string 
                l -= 1
                r +=1
            l = i
            r = i+1
            while l>=0 and r< len(s) and  s[l] == s[r]:
                curr = s[l:r+1]
                if curr == curr[len(s)-1::-1]:
                    sett.add( (i, curr) )
                l-=1
                r+=1

        return len(sett) 
        