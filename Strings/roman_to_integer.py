class Solution:
    def romanToInt (self, s: str) -> int:
        num, i = 0, len(s) - 1
        while (i >= 0):
            if (s[i] == 'I'): num += 1
            elif (s[i] == 'V'):
                if (((i - 1) >= 0) and (s[i - 1] == 'I')): num, i = num + 4, i - 1
                else: num += 5
            elif (s[i] == 'X'):
                if (((i - 1) >= 0) and (s[i - 1] == 'I')): num, i = num + 9, i - 1
                else: num += 10
            elif (s[i] == 'L'):
                if (((i - 1) >= 0) and (s[i - 1] == 'X')): num, i = num + 40, i - 1
                else: num += 50
            elif (s[i] == 'C'):
                if (((i - 1) >= 0) and (s[i - 1] == 'X')): num, i = num + 90, i - 1
                else: num += 100
            elif (s[i] == 'D'):
                if (((i - 1) >= 0) and (s[i - 1] == 'C')): num, i = num + 400, i - 1
                else: num += 500
            else:
                if (((i - 1) >= 0) and (s[i - 1] == 'C')): num, i = num + 900, i - 1
                else: num += 1000
            i -= 1
        return num
