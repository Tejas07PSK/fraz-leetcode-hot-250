class Solution:
    def integerBreak (self, n: int) -> int:
        if (n == 2): return 1
        if (n == 3): return 2
        temp = n // 3
        rem = n % 3
        if (rem == 1):
            rem = 4
            temp -= 1
        elif (rem == 0): rem = 1
        return (3 ** temp) * rem
