class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        given an integer n 
        
        i need to count te number of 1's in binary representation for all numbers 0 to given
        
        and we output an arrray where ith index represents number i 

        """

        if n == 0:
            return [0] 
        if n == 1:
            return [0,1]

        output = [0]*(n+1) #array of size n 
        
        output[1] = 1
        output[2] = 1
        mostSig = 2
        for i in range(3,n+1):
            if mostSig*2 == i:
                mostSig *=2
            remainder = i - mostSig
            output[i] = 1 + output[remainder]

            
        return output