class Solution:
    def isPalindrome (self, x: int) -> bool:
        if (x < 0): return False
        n, x_rev = x, 0
        while (n > 0):
            x_rev = ((x_rev * 10) + (n % 10))
            n //= 10
        return x_rev == x
