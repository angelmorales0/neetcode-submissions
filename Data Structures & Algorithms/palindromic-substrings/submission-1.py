class Solution:
    def countSubstrings(self, s: str) -> int:
        #
        ret = 0 

        #Loop thru every char using the current character as the center and then expand ou to make it such that the next is also a palindrome 
        #cuts down on time complexity since you dont need to check if is a palindrome since we KNOW it is 

        for i in range(len(s)): #odd
            l = i
            r = i
            while l >=0 and r < len(s):

                if s[l] != s[r]:
                    break
         
                ret +=1
                l-=1
                r+=1
        
        for l in range (len(s)): #even case
            r = l+1
            while l >=0 and r < len(s):
 
                if s[l] != s[r]:
                    break
         
                ret +=1
                l-=1
                r+=1 
        
                
        return ret
            





