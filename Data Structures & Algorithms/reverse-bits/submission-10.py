class Solution:
    def reverseBits(self, n: int) -> int:

        """
        given a 32 bit unsigned integer 
        need to revese bit order 
        and return that integer as an output
        """
        ret = 0 

        for i in range(32):
            bit = n >> i & 1 
            if bit:
                ret += bit
            ret = ret <<1
        ret = ret >>1
        
        return ret
