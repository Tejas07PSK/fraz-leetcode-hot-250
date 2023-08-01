class Solution:
    def countDigitOne (self, n: int) -> int:
        i, ans = 1, 0
        while (i <= n):
            ans += ((n // (i * 10)) * i) + min(max((n % (i * 10)) - i + 1, 0), i)
            i *= 10
        return ans
