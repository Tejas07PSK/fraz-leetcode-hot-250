class Solution:
    def countSquares (self, matrix: List[List[int]]) -> int:
        ans, dp = 0, [[0 for j in range(len(matrix[0]) + 1)] for i in range(2)]
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                dp[0][j] = 0
                if (matrix[i][j] == 1):
                    dp[0][j] = 1 + min(dp[0][j + 1], dp[1][j], dp[1][j + 1])
                    ans += dp[0][j]
            dp[0], dp[1] = dp[1], dp[0]
        return ans
