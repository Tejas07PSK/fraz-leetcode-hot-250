class Solution:
    def __method1 (self, prices):
        dp = [[0 for j in range(len(prices))] for i in range(2)]
        for i in range(1, 3):
            mx_diff = -prices[0]
            for j in range(1, len(prices)):
                dp[1][j] = max(dp[1][j - 1], (mx_diff + prices[j]))
                mx_diff = max(mx_diff, (dp[0][j] - prices[j]))
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][-1]

    def __method2 (self, prices):
        buy, prfts = 0, [0 for i in range(len(prices) + 1)]
        for sell in range(1, len(prices)):
            if (prices[sell] < prices[buy]): buy, prfts[sell] = sell, prfts[sell - 1]
            else: prfts[sell] = max(prfts[sell - 1], (prices[sell] - prices[buy]))
        sell = len(prices) - 1
        for buy in range(len(prices) - 2, -1, -1):
            if (prices[buy] > prices[sell]): sell, prfts[buy] = buy, prfts[buy + 1]
            else: prfts[buy] = max(prfts[buy + 1], (prfts[buy - 1] + (prices[sell] - prices[buy])))
        return prfts[0]

    def maxProfit (self, prices: List[int]) -> int:
        return self.__method2(prices)
        #return self.__method1(prices)
