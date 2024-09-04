class Solution:
    def str_rev_generator (self, string):
        ignore = 0
        for ch in reversed(string):
            if (ch == '#'): ignore += 1
            elif (ignore > 0): ignore -= 1
            else: yield ch

    def backspaceCompare (self, s: str, t: str) -> bool:
        itr1, itr2 = self.str_rev_generator(s), self.str_rev_generator(t)
        val1, val2 = next(itr1, None), next(itr2, None)
        while ((val1 != None) and (val2 != None)):
            if (val1 != val2): return False
            val1, val2 = next(itr1, None), next(itr2, None)
        return val1 == val2
