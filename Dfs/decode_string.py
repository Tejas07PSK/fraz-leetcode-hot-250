class Solution:
    def decodeString (self, s: str) -> str:
        stk, i = deque(), 0
        while (i < len(s)):
            if (s[i].isalpha()):
                temp_res = []
                while ((i < len(s)) and (s[i].isalpha())):
                    temp_res.append(s[i])
                    i += 1
                if ((stk) and (isinstance(stk[-1], list))): stk[-1].extend(temp_res)
                else: stk.append(temp_res)
            elif (s[i].isdigit()):
                num = 0
                while ((i < len(s)) and (s[i].isdigit())):
                    num = num * 10 + int(s[i])
                    i += 1
                stk.append(num)
            elif (s[i] == '['):
                stk.append('[')
                i += 1
            else:
                tmp_lst = stk.pop()
                stk.pop()
                num = stk.pop()
                tmp_lst = num * tmp_lst
                if ((stk) and (isinstance(stk[-1], list))): stk[-1].extend(tmp_lst)
                else: stk.append(tmp_lst)
                i += 1
        while (len(stk) > 1):
            temp_lst = stk.pop()
            stk[-1].extend(temp_lst)
        return "".join(stk.pop())
