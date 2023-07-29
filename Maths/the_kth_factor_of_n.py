from math import ceil, floor

class Solution:
    def kthFactor (self, n: int, k: int) -> int:
        for i in range(1, ceil(sqrt(n))):
            if ((n % i) == 0):
                if ((k - 1) == 0): return i
                k -= 1
        for i in range(floor(sqrt(n)), 0, -1):
            if ((n % (n // i)) == 0):
                if ((k - 1) == 0): return n // i
                k -= 1
        return -1
