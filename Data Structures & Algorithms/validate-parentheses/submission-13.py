class Solution:
    def isValid(self, s: str) -> bool:
        #brackets must be closed by the same bracket -> closed in the correct orded 
        #correct order meanss most recent bracket is same type (open)

        mapp = {"}":"{", "]":"[", ")":"("}
        stack = []


        for c in s:
            if c in mapp:
                if stack and mapp[c] == stack[-1]:
                    stack.pop() #pops off top right?
                else:
                    return False
            else:
                stack.append(c)

            
        return False if stack else True