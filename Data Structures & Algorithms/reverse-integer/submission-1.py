class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        ret = 0
    
        while x > 0:
            lastDigit = x % 10
            ret = ret*10 + lastDigit
            x = x // 10
        if is_negative:
            ret = ret*-1
        if ret < -2**31 or ret > 2**31-1:
            return 0
        return ret
