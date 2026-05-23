class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {"(" : ")","[" : "]","{" : "}"}
        for char in s:
            if char in "({[" :# then it is a open parenthesis so we add it to the stack
                stack.append(char)
            else:  # char is closed so we much edit our stack 
                if not stack:
                    return False

                if stack:
                    if char != close_map[stack[-1]]:
                        return False
                    else:
                        stack.pop()
        if stack == []:
            return True
        else:
            return False


#if stack returns true if it exists / is populated
#if not stack returns true if it doesnt exist/ is empty 
        