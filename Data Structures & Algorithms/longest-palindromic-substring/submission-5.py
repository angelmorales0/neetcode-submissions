class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            l,r= i,i
            #odd case
            while l>=0 and r< len(s) and s[l] == s[r]:
                if r-l+1 > len(ret):
                    ret = s[l:r+1]
                l-=1
                r+=1
            #even check 
            l,r = i-1,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > len(ret):
                    ret = s[l:r+1]
                l-=1
                r+=1
        return ret

        