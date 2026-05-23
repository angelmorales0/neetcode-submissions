class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        s=newStr

        l=0
        r=len(s)-1
        while l<=r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True 