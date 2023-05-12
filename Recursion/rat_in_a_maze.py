from collections import deque

class Solution:
    def __findPathHelper (self, row, col, m, n):
        if (m[row][col] == 0): return
        if ((row == (n - 1)) and (col == (n - 1))):
            self.res.append("".join(self.temp_sol))
            return
        m[row][col] = 0
        for row_offset, col_offset, symb in self.dirs:
            next_row, next_col = row + row_offset, col + col_offset
            if ((0 <= next_row < n) and (0 <= next_col < n)):
                self.temp_sol.append(symb)
                self.__findPathHelper(next_row, next_col, m, n)
                self.temp_sol.pop()
        m[row][col] = 1

    def findPath (self, m, n):
        self.res, self.temp_sol = [], deque()
        self.dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
        self.__findPathHelper(0, 0, m, n)
        return self.res
