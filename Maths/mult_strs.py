class Solution:
    def multiply (self, num1: str, num2: str) -> str:
        if ((num1 == "0") or (num2 == "0")): return "0"
        res = [0 for i in range(len(num1) + len(num2))]
        if (len(num2) > len(num1)): num1, num2 = num2, num1
        idx = len(res) - 1
        for i in range(len(num2) - 1, -1, -1):
            k, carr = idx, 0
            for j in range(len(num1) - 1, -1, -1):
                temp = ((ord('0') - ord(num2[i])) * (ord('0') - ord(num1[j]))) + carr + res[k]
                carr = temp // 10
                res[k] = temp % 10
                k -= 1
            res[k] += carr
            idx -= 1
        i = 0
        while ((i < len(res)) and (res[i] == 0)): i += 1
        return "".join(map(str, res[i:]))
