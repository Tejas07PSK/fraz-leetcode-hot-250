class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp_strs = [[] for i in range(numRows)]
        row_cntr, i = 0, 0
        while (i < len(s)):
            while ((i < len(s)) and (row_cntr < numRows)):
                temp_strs[row_cntr].append(s[i])
                i += 1 ; row_cntr += 1
            row_cntr -= 2
            while ((i < len(s)) and (row_cntr > 0)):
                temp_strs[row_cntr].append(s[i])
                i += 1 ; row_cntr -= 1
        return "".join(map(lambda x : "".join(x), temp_strs))
