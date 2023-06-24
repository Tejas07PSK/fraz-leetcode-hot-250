from collections import deque

class Solution:
    def minRemoveToMakeValid (self, s: str) -> str:
        ch_arr = list(s)
        stk = deque()
        for i in range(len(ch_arr)):
            if ((ch_arr[i] != '(') and (ch_arr[i] != ')')): continue
            if (ch_arr[i] == '('): stk.append(i)
            else:
                if (stk and (ch_arr[stk[-1]] == '(')): stk.pop()
                else: stk.append(i)
        while (stk): ch_arr[stk.pop()] = ''
        return "".join(ch_arr)
