from collections import deque

class Solution:
    def calculate (self, s: str) -> int:
        i, q = 0, deque()
        q.append(0)
        while (i < len(s)):
            if (s[i] in '0123456789'):
                d = 0
                while ((i < len(s)) and (s[i] in '0123456789')):
                    d = d * 10 + int(s[i])
                    i += 1
                if (q[0] == '-'):
                    q.append(q.pop() - d) ; q.popleft()
                else: q.append(q.pop() + d)
            elif (s[i] == '+'): i += 1
            elif (s[i] == '-'):
                q.appendleft('-')
                i += 1
            elif (s[i] == '('):
                q.appendleft('(')
                q.append(0)
                i += 1
            elif (s[i] == ')'):
                q.popleft()
                if (q[0] == '-'):
                    q.append(-q.pop() + q.pop()) ; q.popleft()
                else: q.append(q.pop() + q.pop())
                i += 1
            else: i += 1
        return q[-1]
