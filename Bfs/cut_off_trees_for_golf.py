from collections import deque
from heapq import heappush, heappop

class Solution:
    def __bfs (self, start_row, start_col, end_row, end_col, grid):
        dirs, q = [(0, 1), (1, 0), (0, -1), (-1, 0)], deque([(start_row, start_col, 0)])
        visited = set([(start_row, start_col)])
        while (q):
            curr_row, curr_col, curr_jumps = q.popleft()
            if ((curr_row == end_row) and (curr_col == end_col)): return curr_jumps
            for row_offset, col_offset in dirs:
                next_row, next_col, next_jumps = curr_row + row_offset, curr_col + col_offset, curr_jumps + 1
                if ((0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0])) and ((next_row, next_col) not in visited) and (grid[next_row][next_col] > 0)):
                    q.append((next_row, next_col, next_jumps))
                    visited.add((next_row, next_col))
        return -1

    def cutOffTree (self, forest: List[List[int]]) -> int:
        hp = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if (forest[i][j] > 1): heappush(hp, (forest[i][j], i, j))
        steps, curr_row, curr_col = 0, 0, 0
        while (hp):
            cell_height, dest_row, dest_col = heappop(hp)
            temp_steps = self.__bfs(curr_row, curr_col, dest_row, dest_col, forest)
            if (temp_steps == -1): return -1
            steps, curr_row, curr_col = steps + temp_steps, dest_row, dest_col
        return steps
