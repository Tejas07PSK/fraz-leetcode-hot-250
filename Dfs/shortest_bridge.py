class Solution:
    def shortestBridge (self, grid: List[List[int]]) -> int:
        q1, q2, dirs, flag = deque(), deque(), [(0, 1), (0, -1), (1, 0), (-1, 0)], False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    flag = True
                    q1.append((i, j)) ; grid[i][j] = -1
                    while (q1):
                        curr_i, curr_j = q1.popleft()
                        for i_offset, j_offset in dirs:
                            next_i, next_j = curr_i + i_offset, curr_j + j_offset
                            if ((0 <= next_i < len(grid)) and (0 <= next_j < len(grid[0]))):
                                if (grid[next_i][next_j] == 1):
                                    q1.append((next_i, next_j))
                                    grid[next_i][next_j] = -1
                                elif (grid[next_i][next_j] == 0):
                                    q2.append((next_i, next_j, 0))
                                    grid[next_i][next_j] = -1
                    break
            if (flag): break
        dist, flag = 0, False
        while (q2):
            curr_i, curr_j, curr_dist = q2.popleft()
            for i_offset, j_offset in dirs:
                next_i, next_j, next_dist = curr_i + i_offset, curr_j + j_offset, curr_dist + 1
                if ((0 <= next_i < len(grid)) and (0 <= next_j < len(grid[0]))):
                    if (grid[next_i][next_j] == 1):
                        flag = True
                        dist = next_dist
                        break
                    elif (grid[next_i][next_j] == 0):
                        q2.append((next_i, next_j, next_dist))
                        grid[next_i][next_j] = -1
            if (flag): break
        return dist
