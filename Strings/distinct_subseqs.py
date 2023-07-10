class Solution:
    def numDistinct (self, s: str, t: str) -> int:
        dp = [[1 for j in range(len(s) + 1)] for i in range(2)]
        for i in range(len(t) - 1, -1, -1):
            dp[0][-1] = 0
            for j in range(len(s) - 1, -1, -1):
                dp[0][j] = 0
                if (s[j] == t[i]): dp[0][j] = dp[1][j + 1] 
                dp[0][j] += dp[0][j + 1]
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][0]
