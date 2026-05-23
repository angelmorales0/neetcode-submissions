class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # right side is the top of the stack, filled with temp & index
        result = [0]*len(temperatures)

        for index in range(len(temperatures)):
            if stack == []:
                stack.append([temperatures[index], index])
            else:
                while stack != [] and temperatures[index] > stack[-1][0]: # while curr temp is greater than old temp we must pop from stack and edit array 
                    result[stack[-1][1]] = index - stack[-1][1]
                    stack.pop()
                stack.append([temperatures[index], index])
        return result