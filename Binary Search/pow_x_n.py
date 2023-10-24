class Solution:
    def myPow (self, x: float, n: int) -> float:
        if (n == 0): return 1
        if (n < 0):
            x = 1 / x
            n = -n
        res, mask = 1, 1
        while (n > 0):
            if ((n & mask) == 1): res *= x
            x *= x
            n >>= 1
        return res
