class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""

        for i in range(len(s)): # odd case
            l = r= i
        
            while r < len(s) and l >= 0 : #while is palindrome
                if s[l] != s[r]:
                    break
                if r-l+1 >= len(ret):
                    ret = s[l:r+1]
                l -= 1 
                r+=1 

        for i in range(len(s)): # even case
            l = i
            r= i+1
            while r < len(s) and l >= 0: #while is palindrome
                if s[l] != s[r]:
                    break
                if r-l+1 >= len(ret):
                    ret = s[l:r+1]
                l -= 1 
                r+=1 
        return ret 

            