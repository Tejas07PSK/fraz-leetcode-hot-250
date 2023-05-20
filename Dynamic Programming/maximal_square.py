class Solution:
    def __method1 (self, i, j, matrix):
        if ((i == len(matrix)) or (j == len(matrix[0]))): return 0
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = 0
        if (matrix[i][j] != '0'):
            self.dp[i][j] = 1 + min(
                self.__method1(i, j + 1, matrix),
                self.__method1(i + 1, j + 1, matrix),
                self.__method1(i + 1, j, matrix)
            )
        return self.dp[i][j]

    def __method1_handler (self, matrix):
        self.dp = [[None for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.__method1(i, j, matrix)
                self.ans = max(self.ans, self.dp[i][j])
        return self.ans * self.ans

    def __method2 (self, matrix):
        self.dp = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if (matrix[i][j] != '0'):
                    self.dp[i][j] = 1 + min(self.dp[i][j + 1], self.dp[i + 1][j + 1], self.dp[i + 1][j])
                    self.ans = max(self.ans, self.dp[i][j])
        return self.ans * self.ans

    def __method3 (self, matrix):
        self.dp = [[0 for j in range(len(matrix[0]) + 1)] for i in range(2)]
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                self.dp[0][j] = 0
                if (matrix[i][j] != '0'):
                    self.dp[0][j] = 1 + min(self.dp[0][j + 1], self.dp[1][j + 1], self.dp[1][j])
                    self.ans = max(self.ans, self.dp[0][j])
            self.dp[0], self.dp[1] = self.dp[1], self.dp[0]
        return self.ans * self.ans

    def maximalSquare (self, matrix: List[List[str]]) -> int:
        self.ans = 0
        #return self.__method1_handler(matrix)
        #return self.__method2(matrix)
        return self.__method3(matrix)
