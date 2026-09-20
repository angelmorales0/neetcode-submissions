class Solution:
    def getSum(self, a: int, b: int) -> int:

        noncarries = a ^ b
        carries = a & b
        carries = carries <<1
        # a = 01
        # b= 01
        #carries = 0 
        #noncarries = 1
        
        return carries+noncarries
    
        # ^ = xor 
        # & = and 

   