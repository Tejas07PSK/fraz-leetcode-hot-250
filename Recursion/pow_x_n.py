class Solution:
    def __method1 (x, n):
        if (n < 0): x, n =  1 / x, -n
        if (n == 0): return 1
        if (n == 1): return x
        if ((n % 2) == 1): return x * self.myPow((x * x), (n // 2))
        return self.myPow((x * x), (n // 2))

    def __method2 (x, n):
        if (n < 0): x, n =  1 / x, -n
        if (n == 0): return 1
        res = 1
        while (n >= 2):
            if ((n % 2) == 1): res *= x
            x *= x
            n //= 2
        res *= x
        return res

    def myPow (self, x: float, n: int) -> float:
        return self.__method2(x, n)
        # return self.__method1(x, n)
