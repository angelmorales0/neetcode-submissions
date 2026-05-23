class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #could go through 1-1 which is p inefficent need to do one pass instead of 2 can store using stack?

        #What condition is met?
        #[30,38,30,36,35,40,28] we can just continue until we hit a warmer date than current and add that to the list 
        #and if hit then we can edit our list since all lower values still get hit y this 
        #30:1, 38

        #optimal = if temp is 0 for a higher temp then our temp must be 0, leave early
        #2,1,1,3


        #
        #
        #
        #


        #top is always the smallest value 
        #68
        

        
        #36
        #30
        #38

        stack = [] #temp index
        ret = [0] * (len(temperatures))

        if temperatures:
            stack.append([temperatures[0],0])
        for i in range(1,len(temperatures)):
            count = 0
            while stack and temperatures[i] > stack[-1][0]:
                #edge case stack is empty 
                temp, index = stack.pop()
                ret[index] = i - index 

            stack.append([temperatures[i],i])
        return ret
