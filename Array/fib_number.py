class Solution:
    def fib (self, n: int) -> int:
        if (n == 0): return 0
        if (n == 1): return 1
        prev, prev_prev = 0, 1
        for i in range(2, n + 1):
            temp = prev + prev_prev
            prev = prev_prev
            prev_prev = temp
        return prev_prev
