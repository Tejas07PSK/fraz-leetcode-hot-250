class Solution:
    def addStrings (self, num1: str, num2: str) -> str:
        new_num, carr = [], 0
        if (len(num2) > len(num1)): num1, num2 = num2, num1
        for i in range(1, len(num2) + 1):
            curr_num = int(num1[-i]) + int(num2[-i]) + carr
            new_num.append(str(curr_num % 10))
            carr = curr_num // 10
        for i in range(i + 1, len(num1) + 1):
            curr_num = int(num1[-i]) + carr
            new_num.append(str(curr_num % 10))
            carr = curr_num // 10
        if (carr > 0): new_num.append(str(carr))
        return "".join(reversed(new_num))
