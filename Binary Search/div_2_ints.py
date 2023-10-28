class Solution:
    def divide (self, dividend: int, divisor: int) -> int:
        pos = ((dividend < 0) == (divisor < 0))
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while (dividend >= divisor):
            temp, n = divisor, 1
            while ((temp << 1) <= dividend):
                temp <<= 1
                n <<= 1
            ans += n
            dividend -= temp
        if (not pos): ans = -ans
        return min(max(-2147483648, ans), 2147483647)
