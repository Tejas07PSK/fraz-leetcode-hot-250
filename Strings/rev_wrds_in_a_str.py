from collections import deque

class Solution:
    def reverseWords (self, s: str) -> str:
        i, res = 0, deque()
        while (i < len(s)):
            if (s[i] == ' '):
                while (((i + 1) < len(s)) and (s[i + 1] == s[i])): i += 1
            else:
                temp_ch_arr = [s[i]]
                while (((i + 1) < len(s)) and (s[i + 1] != ' ')):
                    temp_ch_arr.append(s[i + 1])
                    i += 1
                res.appendleft(''.join(temp_ch_arr))
            i += 1
        return ' '.join(res)
