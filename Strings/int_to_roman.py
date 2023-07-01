from collections import deque
class Solution:
    def intToRoman (self, num: int) -> str:
        n, digit, place = num, 0, 1
        res = deque()
        while (n > 0):
            digit = n % 10
            if (1 <= digit <= 3):
                symb = ''
                if (place == 1): symb = 'I'
                elif (place == 2): symb = 'X'
                elif (place == 3): symb = 'C'
                else: symb = 'M'
                for i in range(digit): res.appendleft(symb)
            elif (digit == 4):
                symb = ''
                if (place == 1): symb = 'IV'
                elif (place == 2): symb = 'XL'
                elif (place == 3): symb = 'CD'
                else: symb = 'MMMM'
                res.appendleft(symb)
            elif (digit == 5):
                symb = ''
                if (place == 1): symb = 'V'
                elif (place == 2): symb = 'L'
                elif (place == 3): symb = 'D'
                else: symb = 'MMMMM'
                res.appendleft(symb)
            elif (6 <= digit <= 8):
                symb, base = '', ''
                if (place == 1): symb, base = 'I', 'V'
                elif (place == 2): symb, base = 'X', 'L'
                elif (place == 3): symb, base = 'C', 'D'
                else: symb, base = 'M', 'MMMMM'
                for i in range(digit - 5): res.appendleft(symb)
                res.appendleft(base)
            elif (digit == 9):
                symb = ''
                if (place == 1): symb = 'IX'
                elif (place == 2): symb = 'XC'
                elif (place == 3): symb = 'CM'
                else: symb = 'MMMMMMMMM'
                res.appendleft(symb)
            place += 1
            n //= 10
        return "".join(res)
