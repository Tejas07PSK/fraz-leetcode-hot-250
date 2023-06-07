class Solution:
    def maxProfit (self, k: int, prices: List[int]) -> int:
        dp = [[0 for j in range(len(prices))] for i in range(2)]
        for i in range(1, k + 1):
            maxDiff, dp[1][0] = -prices[0], 0
            for j in range(1, len(prices)):
                dp[1][j] = max(dp[1][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[0][j - 1] - prices[j])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][-1]
