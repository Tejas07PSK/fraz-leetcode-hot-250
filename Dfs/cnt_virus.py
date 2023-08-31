from collections import deque

class Solution:
    def __bfs_helper (self, grid):
        cont_zones, free_adj_zones, possible_walls, tot_cont_cells = [], [], [], 0
        seen = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if ((grid[row][col] == 1) and (not seen[row][col])):
                    tot_cont_cells += 1
                    curr_cont_zone, curr_possible_walls, curr_free_adj_zone = [(row, col)], 0, set()
                    q = deque() ; q.append((row, col))
                    seen[row][col] = True
                    while (q):
                        curr_row, curr_col = q.popleft()
                        for row_offset, col_offset in self.dirs:
                            next_row, next_col = curr_row + row_offset, curr_col + col_offset
                            if ((0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0]))):
                                if ((grid[next_row][next_col] == 1) and (not seen[next_row][next_col])):
                                    tot_cont_cells += 1
                                    q.append((next_row, next_col))
                                    seen[next_row][next_col] = True
                                    curr_cont_zone.append((next_row, next_col))
                                elif (grid[next_row][next_col] == 0):
                                    curr_free_adj_zone.add((next_row, next_col))
                                    curr_possible_walls += 1
                    cont_zones.append(curr_cont_zone)
                    free_adj_zones.append(curr_free_adj_zone)
                    possible_walls.append(curr_possible_walls)
        return cont_zones, free_adj_zones, possible_walls, tot_cont_cells

    def containVirus (self, isInfected: List[List[int]]) -> int:
        ans, self.dirs = 0, [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cont_zones, free_adj_zones, possible_walls, tot_cont_cells = self.__bfs_helper(isInfected)
        while (cont_zones):
            if (tot_cont_cells == (len(isInfected) * len(isInfected[0]))): return ans
            risky_zone_idx = 0
            for i in range(1, len(cont_zones)):
                if (len(free_adj_zones[i]) > len(free_adj_zones[risky_zone_idx])): risky_zone_idx = i
            ans += possible_walls[risky_zone_idx]
            for row, col in cont_zones[risky_zone_idx]: isInfected[row][col] = 2
            for i in range(len(cont_zones)):
                if (i != risky_zone_idx):
                    for row, col in free_adj_zones[i]: isInfected[row][col] = 1
            cont_zones, free_adj_zones, possible_walls, tot_cont_cells = self.__bfs_helper(isInfected)
        return ans
