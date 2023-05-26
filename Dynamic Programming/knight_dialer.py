class Solution:
    def __method1 (self, i, j, n):
        if (n == 1): return 1
        if (self.dp[i][j][n] != None): return self.dp[i][j][n]
        self.dp[i][j][n] = 0
        for row_offset, col_offset in self.dirs:
            next_i, next_j = i + row_offset, j + col_offset
            if ((next_i >= 4) or (next_i < 0) or (next_j >= 3) or (next_j < 0) or ((next_i == 3) and ((next_j == 0) or (next_j == 2)))): continue
            self.dp[i][j][n] = (self.dp[i][j][n] + self.__method1(next_i, next_j, n - 1)) % self.mod
        return self.dp[i][j][n]

    def __method1_handler (self, n):
        self.dp = [[[None for k in range(n + 1)] for j in range(3)] for i in range(4)]
        self.dirs = [(1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1)]
        self.mod = 1000000007
        ans = 0
        for i in range(4):
            for j in range(3):
                if ((i == 3) and ((j == 0) or (j == 2))): continue
                ans = (ans + self.__method1(i, j, n)) % self.mod
        return ans

    def __method2 (self, n):
        graph = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        mod = 1000000007
        curr_num_count = [1 for i in range(10)]
        for i in range(n - 1):
            next_num_count = [0 for i in range(10)]
            for j in range(10):
                for k in graph[j]: next_num_count[k] = (next_num_count[k] + curr_num_count[j]) % mod
            del curr_num_count
            curr_num_count = next_num_count
            del next_num_count
        ans = 0
        for i in range(10): ans = (ans + curr_num_count[i]) % mod
        return ans

    def knightDialer (self, n: int) -> int:
        # return self.__method1_handler(n)
        return self.__method2(n)
