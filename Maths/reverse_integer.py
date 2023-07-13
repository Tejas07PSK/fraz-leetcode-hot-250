class Solution:
    def reverse (self, x: int) -> int:
        sign = 1
        if (x < 0):
            x = -x
            sign = -sign
        result, start = 0, 2 ** 31
        end = start - 1
        while (x > 0):
            digit = x % 10
            result = result * 10 + digit
            if ((sign == -1) and (result > start)): return 0
            if ((sign == 1) and (result > end)): return 0
            x //= 10
        return sign * result
