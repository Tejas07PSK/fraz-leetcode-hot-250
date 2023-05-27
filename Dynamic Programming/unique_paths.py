class Solution:
    def uniquePaths (self, m: int, n: int) -> int:
        dp = [[0 for j in range(n + 1)] for i in range(2)]
        dp[1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1): dp[0][j] = dp[1][j] + dp[0][j + 1]
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][0]
