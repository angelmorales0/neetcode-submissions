class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # right side is the top of the stack, filled with temp & index
        result = [0]*len(temperatures)
        for index in range (len(temperatures)):
            if stack == [] :
                stack.append([temperatures[index], index])
            else:
                while stack != [] and temperatures[index] > stack[-1][0]:
                    result[stack[-1][1]] =  index- stack[-1][1]  #is stack -1 1 the res index?
                    stack.pop()
                stack.append([temperatures[index],index])
                
        return result