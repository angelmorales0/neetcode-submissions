class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        given an integer n 
        
        i need to count te number of 1's in binary representation for all numbers 0 to given
        
        and we output an arrray where ith index represents number i 

        """

        output = [0]*(n+1) #array of size n 
        
        for i in range(n+1):
            output[i] = Counter(bin(i))['1']
        return output