class Solution:
    def maxProfit (self, prices: List[int]) -> int:
        min_from_left, curr_mx_prft, ans = prices[0], 0, 0
        for i in range(1, len(prices)):
            if ((prices[i] > min_from_left) and ((prices[i] - min_from_left) >= curr_mx_prft)):
                    curr_mx_prft = prices[i] - min_from_left
            else:
                ans += curr_mx_prft
                curr_mx_prft = 0
                min_from_left = prices[i]
        ans += curr_mx_prft
        return ans
