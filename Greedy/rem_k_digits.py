from collections import deque

class Solution:
    def removeKdigits (self, num: str, k: int) -> str:
        stk = deque()
        for n in num:
            while ((k > 0) and stk and (int(n) < int(stk[-1]))):
                stk.pop()
                k -= 1
            stk.append(n)
        while ((k > 0) and stk):
            stk.pop()
            k -= 1
        if (not stk): stk.append('0')
        while ((len(stk) > 1) and (stk[0] == '0')): stk.popleft()
        return "".join(stk)
