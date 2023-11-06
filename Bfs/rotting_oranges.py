from collections import deque

class Solution:
    def orangesRotting (self, grid: List[List[int]]) -> int:
        normal_oranges, q = 0, deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 2): q.append((i, j))
                elif (grid[i][j] == 1): normal_oranges += 1
        if (not q): return -1 if (normal_oranges > 0) else 0
        time_taken = -1
        while (q):
            curr_size = len(q)
            while (curr_size > 0):
                curr_row, curr_col = q.popleft()
                for row_offset, col_offset in directions:
                    next_row = curr_row + row_offset
                    next_col = curr_col + col_offset
                    if ((0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0])) and (grid[next_row][next_col] == 1)):
                        q.append((next_row, next_col))
                        grid[next_row][next_col] = 2
                        normal_oranges -= 1
                curr_size -= 1
            time_taken += 1
        return -1 if (normal_oranges > 0) else time_taken
