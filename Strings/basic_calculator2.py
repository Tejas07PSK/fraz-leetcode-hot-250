class Solution:
    def calculate (self, s: str) -> int:
        num1, num2, last_exp, i = 0, 0, '+', 0
        while (i < len(s)):
            if (s[i] == ' '):
                i += 1
            elif (s[i] in '+-*/'):
                last_exp = s[i]
                i += 1
            else:
                curr_num = int(s[i])
                while ((i + 1) < len(s)):
                    if (s[i + 1] in ' +-*/'): break
                    else:
                        curr_num = curr_num * 10 + int(s[i + 1])
                        i += 1
                if (last_exp == '+'):
                    num1 += num2
                    num2 = curr_num
                elif (last_exp == '-'):
                    num1 += num2
                    num2 = -curr_num
                elif (last_exp == '*'): num2 *= curr_num
                else:
                    if (num2 < 0):
                        num2 = -num2
                        num2 //= curr_num
                        num2 = -num2
                    else: num2 //= curr_num
                i += 1
        num1 += num2
        return num1
