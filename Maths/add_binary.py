from collections import deque

class Solution:
    def addBinary (self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry, ans = 0, deque()
        while ((i >= 0) or (j >= 0)):
            add_val = carry
            if (i >= 0):
                add_val += ord(a[i]) - ord('0')
                i -= 1
            if (j >= 0):
                add_val += ord(b[j]) - ord('0')
                j -= 1
            ans.appendleft(str(add_val % 2))
            carry = add_val // 2
        if (carry != 0): ans.appendleft(str(carry))
        return "".join(ans)
