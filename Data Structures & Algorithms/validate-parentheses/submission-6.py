class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "([{": #then it is an open bracket so we can add it to our stack
                stack.append(char)
            else: #it must be a closed bracket
                if not stack:
                    return False
                if stack[-1] ==  closed_map[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
