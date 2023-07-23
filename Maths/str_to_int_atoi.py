class Solution:
    def myAtoi (self, s: str) -> int:
        mn, mx, sign, num = -2 ** 31, 2 ** 31 - 1, 1, 0
        i = 0
        while ((i < len(s)) and (s[i] == ' ')): i += 1
        if (i < len(s)):
            if (s[i] == '-'):
                sign = -1
                i += 1
            elif (s[i] == '+'): i += 1
        while (i < len(s)):
            if (not s[i].isnumeric()): break
            num = (num * 10) + (ord(s[i]) - ord('0'))
            if ((num * sign) >= mx): return mx
            if ((num * sign) <= mn): return mn
            i += 1
        return num * sign
