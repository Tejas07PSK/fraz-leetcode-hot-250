class Solution:
    def isPowerOfTwo (self, n: int) -> bool:
        if (n <= 0): return False
        return ((n - 1) & n) == 0
