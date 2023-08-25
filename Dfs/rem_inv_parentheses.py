from collections import deque

class Solution:
    def __method1 (self, idx, lft_cnt, rt_cnt, inv_lft, inv_rt, s, tmp_ans):
        if (idx == len(s)):
            if ((inv_lft == 0) and (inv_rt == 0)): self.res.add("".join(tmp_ans))
            return
        if ((s[idx] == '(') and (inv_lft > 0)): self.__helper(idx + 1, lft_cnt, rt_cnt, inv_lft - 1, inv_rt, s, tmp_ans)
        if ((s[idx] == ')') and (inv_rt > 0)): self.__helper(idx + 1, lft_cnt, rt_cnt, inv_lft, inv_rt - 1, s, tmp_ans)
        tmp_ans.append(s[idx])
        if (s[idx] == '('): self.__helper(idx + 1, lft_cnt + 1, rt_cnt, inv_lft, inv_rt, s, tmp_ans)
        elif (s[idx] == ')'):
            if (lft_cnt > rt_cnt): self.__helper(idx + 1, lft_cnt, rt_cnt + 1, inv_lft, inv_rt, s, tmp_ans)
        else: self.__helper(idx + 1, lft_cnt, rt_cnt, inv_lft, inv_rt, s, tmp_ans)
        tmp_ans.pop()

    def __method1_helper (self, s):
        inv_lft, inv_rt = 0, 0
        for ch in s:
            if (ch == '('): inv_lft += 1
            elif (ch == ')'):
                if (inv_lft == 0): inv_rt += 1
                else: inv_lft -= 1
        self.res = set()
        self.__helper(0, 0, 0, inv_lft, inv_rt, s, [])
        return list(self.res)

    def __isValid(self, s):
        count = 0
        for ch in s:
            if (ch == '('): count += 1
            elif (ch == ')'): count -= 1
            if (count < 0): return False
        return count == 0

    def __method2 (self, s):
        q, visited, res, flag = deque(), set(), [], False
        q.append(s) ; visited.add(s)
        while (q):
            curr_str = q.popleft()
            if (self.__isValid(curr_str)):
                res.append(curr_str)
                flag = True
            if (flag): continue
            for i in range(len(curr_str)):
                if (curr_str[i] in '()'):
                    next_str = curr_str[:i] + curr_str[i + 1:]
                    if (next_str not in visited):
                        q.append(next_str)
                        visited.add(next_str)
        return res

    def removeInvalidParentheses (self, s: str) -> List[str]:
        #return self.__method1_helper(s)
        return self.__method2(s)
