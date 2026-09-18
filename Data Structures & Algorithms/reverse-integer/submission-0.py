class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        ret = 0
        x = abs(x)

        while x > 0:
            digit = x % 10
            ret = ret * 10 + digit
            x //= 10
        if is_negative:
            ret *= -1
        if ret < -2**31 or ret > 2**31:
            return 0
        return ret