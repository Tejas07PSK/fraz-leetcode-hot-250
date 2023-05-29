class NumMatrix:
    def __init__ (self, matrix: List[List[int]]):
        self.dp = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1] + matrix[i][j]

    def sumRegion (self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2][col2] - self.dp[row2][col1 - 1] - self.dp[row1 - 1][col2] + self.dp[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
