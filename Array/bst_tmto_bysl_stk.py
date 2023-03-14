class Solution:
    def maxProfit (self, prices: List[int]) -> int:
        mx_prft, min_from_left = 0, prices[0]
        for i in range(1, len(prices)):
            if (prices[i] > min_from_left):
                mx_prft = max(mx_prft, (prices[i] - min_from_left))
            elif (prices[i] < min_from_left):
                min_from_left = prices[i]
        return mx_prft
