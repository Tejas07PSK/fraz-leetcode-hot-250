from collections import deque

class Solution:
    def __method1 (self, s):
        open_par, close_par, ans = 0, 0, 0
        for ch in s:
            if (ch == '('): open_par += 1
            else: close_par += 1
            if (open_par == close_par): ans = max(ans, (2 * open_par))
            elif (close_par > open_par): open_par = close_par = 0
        open_par, close_par = 0, 0
        for ch in reversed(s):
            if (ch == ')'): close_par += 1
            else: open_par += 1
            if (open_par == close_par): ans = max(ans, (2 * close_par))
            elif (open_par > close_par): open_par = close_par = 0
        return ans

    def __method2 (self, s):
        stk, curr_len, ans = deque(), 0, 0
        for ch in s:
            if (ch == '('):
                stk.append(('(', curr_len + 1))
                curr_len = 0
            elif (stk):
                curr_len += stk.pop()[1] + 1
                ans = max(ans, curr_len)
            else: curr_len = 0
        return ans

    def longestValidParentheses (self, s: str) -> int:
        return self.__method1(s)
        #return self.__method2(s)
