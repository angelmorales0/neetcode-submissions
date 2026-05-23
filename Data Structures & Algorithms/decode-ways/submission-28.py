class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        dp_double = 0
        dp_next = 1

        #FU -> Try to opti using 2 ptr
        for i in range(len(s)-1,-1,-1):
        
            if s[i] == "0":
                current = 0 #cant deocde this bitch tree is cooked 
            # we can decode it atleat using th edefault just number 
            else:
                current = dp_next
            #now we get the multi case
                if (i+1 < len(s) ) and (s[i] == "1" or s[i]=="2" and s[i+1] in "0123456"):
                    current += dp_double
            dp_double = dp_next
            dp_next = current
        return dp_next


