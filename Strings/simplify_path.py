class Solution:
    def simplifyPath (self, path: str) -> str:
        i, stk = 0, deque()
        while (i < len(path)):
            while ((i < len(path)) and (path[i] == '/')): i += 1
            if (i == len(path)): break
            token_start, token_end = i - 1, i - 1
            dot_count, other_count = 0, 0
            while ((i < len(path)) and (path[i] != '/')):
                if (path[i] == '.'): dot_count += 1
                else: other_count += 1
                token_end += 1 ; i += 1
            if ((dot_count == 1) and (other_count == 0)): continue
            if ((dot_count == 2) and (other_count == 0)):
                if (stk): stk.pop()
                continue
            stk.append(path[token_start:token_end + 1])
        return "".join(stk) if (stk) else "/"
