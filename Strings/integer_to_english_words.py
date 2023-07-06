from collections import deque

class Solution:
    def helper (self, digit):
        if (digit == 1): return 'One'
        elif (digit == 2): return 'Two'
        elif (digit == 3): return 'Three'
        elif (digit == 4): return 'Four'
        elif (digit == 5): return 'Five'
        elif (digit == 6): return 'Six'
        elif (digit == 7): return 'Seven'
        elif (digit == 8): return 'Eight'
        elif (digit == 9): return 'Nine'
        else: return ''

    def numberToWords(self, num: int) -> str:
        if (num == 0): return 'Zero'
        place, prev_digit, ans, set_flag = 0, 0, deque(), 0
        while (num > 0):
            digit = num % 10
            if (place == 3): ans.appendleft('Thousand')
            elif (place == 6):
                if (ans[0] == 'Thousand'): ans.popleft()
                ans.appendleft('Million')
            elif (place >= 9):
                if (ans[0] == 'Million'): ans.popleft()
                ans.appendleft('Billion')
            base_place = place % 3
            if (base_place == 0):
                next_digit = (num // 10) % 10
                if (next_digit != 1):
                    if (digit != 0): ans.appendleft(self.helper(digit))
            elif (base_place == 1):
                if (digit == 1):
                    if (prev_digit == 1): ans.appendleft('Eleven')
                    elif (prev_digit == 2): ans.appendleft('Twelve')
                    elif (prev_digit == 3): ans.appendleft('Thirteen')
                    elif (prev_digit == 4): ans.appendleft('Fourteen')
                    elif (prev_digit == 5): ans.appendleft('Fifteen')
                    elif (prev_digit == 6): ans.appendleft('Sixteen')
                    elif (prev_digit == 7): ans.appendleft('Seventeen')
                    elif (prev_digit == 8): ans.appendleft('Eighteen')
                    elif (prev_digit == 9): ans.appendleft('Nineteen')
                    else: ans.appendleft('Ten')
                elif (digit == 2): ans.appendleft('Twenty')
                elif (digit == 3): ans.appendleft('Thirty')
                elif (digit == 4): ans.appendleft('Forty')
                elif (digit == 5): ans.appendleft('Fifty')
                elif (digit == 6): ans.appendleft('Sixty')
                elif (digit == 7): ans.appendleft('Seventy')
                elif (digit == 8): ans.appendleft('Eighty')
                elif (digit == 9): ans.appendleft('Ninety')
            elif (base_place == 2):
                if (digit != 0):
                    ans.appendleft('Hundred')
                    ans.appendleft(self.helper(digit))
            num //= 10
            place += 1
            prev_digit = digit
        return " ".join(ans)
