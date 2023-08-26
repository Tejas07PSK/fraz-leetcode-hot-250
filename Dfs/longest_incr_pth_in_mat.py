from collections import deque

class Solution:
    def __method1 (self, matrix):
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        in_degs = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                for row_offset, col_offset in dirs:
                    next_row, next_col = row + row_offset, col + col_offset
                    if ((0 <= next_row < len(matrix)) and (0 <= next_col < len(matrix[0])) and (matrix[row][col] > matrix[next_row][next_col])): in_degs[row][col] += 1
        q, path_size = deque(), 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (in_degs[row][col] == 0): q.append((row, col))
        while (q):
            curr_q_len = len(q)
            for i in range(curr_q_len):
                curr_row, curr_col = q.popleft()
                for row_offset, col_offset in dirs:
                    next_row, next_col = curr_row + row_offset, curr_col + col_offset
                    if ((0 <= next_row < len(matrix)) and (0 <= next_col < len(matrix[0])) and (matrix[curr_row][curr_col] < matrix[next_row][next_col])):
                        in_degs[next_row][next_col] -= 1
                        if (in_degs[next_row][next_col] == 0): q.append((next_row, next_col))
            path_size += 1
        return path_size

    def __method2 (self, curr_row, curr_col, matrix):
        if (self.dp[curr_row][curr_col] != None): return self.dp[curr_row][curr_col]
        ans = 1
        for row_offset, col_offset in self.dirs:
            next_row, next_col = curr_row + row_offset, curr_col + col_offset
            if ((0 <= next_row < len(matrix)) and (0 <= next_col < len(matrix[0])) and (matrix[curr_row][curr_col] > matrix[next_row][next_col])): ans = max(ans, 1 + self.__method2(next_row, next_col, matrix))
        self.dp[curr_row][curr_col] = ans
        return ans

    def __method2_handler (self, matrix):
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.dp = [[None for j in range(len(matrix[0]))] for i in range(len(matrix))]
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans = max(ans, self.__method2(row, col, matrix))
        return ans

    def longestIncreasingPath (self, matrix: List[List[int]]) -> int:
        #return self.__method1(matrix)
        return self.__method2_handler(matrix)
