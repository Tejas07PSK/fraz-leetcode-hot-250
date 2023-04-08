class Solution:
    def __dfs_helper (self, i, j, grid):
        self.curr_sz += 1
        grid[i][j] = -grid[i][j]
        for row_offset, col_offset in self.dirs:
            next_i, next_j = i + row_offset, j + col_offset
            if ((0 <= next_i < len(grid)) and (0 <= next_j < len(grid[0])) and (grid[next_i][next_j] == 1)):
                self.__dfs_helper(next_i, next_j, grid)

    def __method1 (self, grid):
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans, self.curr_sz = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    self.__dfs_helper(i, j, grid)
                    ans = max(ans, self.curr_sz)
                    self.curr_sz = 0
        return ans

    def maxAreaOfIsland (self, grid: List[List[int]]) -> int:
        return self.__method1(grid)
