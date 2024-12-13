class Solution:
    def removeDuplicates (self, s: str, k: int) -> str:
        stk = []
        for i in range(len(s)):
            ch = s[i]
            if ((stk) and (ch == stk[-1][0])): stk[-1][1] += 1
            else: stk.append([ch, 1])
            stk[-1][1] = stk[-1][1] % k
            if (stk[-1][1] == 0): stk.pop()
        return "".join(["".join([ch] * cnt) for ch, cnt in stk])
