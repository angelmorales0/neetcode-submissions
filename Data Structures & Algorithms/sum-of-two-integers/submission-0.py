class Solution:
    def getSum(self, a: int, b: int) -> int:
        carries = ((a & b ) << 1)#need to make it shift left
        nonCarries = a ^ b  
    # xor + and is equivlent to addition!

        return carries + nonCarries