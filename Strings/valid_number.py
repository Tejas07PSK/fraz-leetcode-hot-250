class Solution:
    def isNumber (self, s: str) -> bool:
        digits_seen, dot_seen, e_seen = False, False, False
        for i in range(len(s)):
            ch = s[i]
            if (ch in '0123456789'):
                digits_seen = True
            elif (ch == '.'):
                if (dot_seen or e_seen): return False
                dot_seen = True
            elif (ch in 'eE'):
                if (e_seen or (not digits_seen)): return False
                e_seen = True
                digits_seen = False
            elif (ch in '+-'):
                if ((i != 0) and (s[i - 1] not in 'eE')): return False
            else: return False
        return digits_seen
