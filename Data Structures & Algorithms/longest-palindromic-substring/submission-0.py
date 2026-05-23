class Solution:
    def longestPalindrome(self, s: str) -> str:
        #sliding window type shi???
        ret = ""

        for i in range(len(s)):
            l= i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]: #since we go out    
                length = r-l+1
                if length > len(ret):
                    ret = s[l:r+1]
                l -= 1
                r +=1
            #for odd nums above 
            #for even below 
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l+1
                if length > len(ret):
                    ret = s[l:r+1]
                r+=1
                l-=1
            
        return ret


                

            #if it is palindrome, see if it still is one with the next 
            
        