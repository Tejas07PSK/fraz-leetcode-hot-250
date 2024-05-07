class Solution:
    def __helper (self, row, col, grid, blanks):
        if (grid[row][col] == 2): return 1 if (blanks == 0) else 0
        temp = grid[row][col]
        grid[row][col] = -1
        ans = 0
        for row_offset, col_offset in self.direcs:
            next_row, next_col = row + row_offset, col + col_offset
            if ((0 <= next_row < self.rows) and (0 <= next_col < self.cols) and (grid[next_row][next_col] != -1)):
                ans += self.__helper(next_row, next_col, grid, blanks - 1)
        grid[row][col] = temp
        return ans

    def uniquePathsIII (self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start_row, start_col, start_idx, ans, blanks = 0, 0, 0, 0, 0
        for i in range(self.rows):
            for j in range(self.cols):
                if (grid[i][j] == 1): start_row, start_col = i, j
                if ((grid[i][j] != -1) and (grid[i][j] != 2)): blanks += 1
        return self.__helper(start_row, start_col, grid, blanks)
