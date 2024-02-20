class Solution:
    def countArrangement (self, n: int) -> int:
        m =  (1 << n) - 1
        dp = [[0 if (i == 0) else 1 for j in range(m + 1)] for i in range(2)]
        for pos in range(n, 0, -1):
            for bitmap in range(m, -1, -1):
                curr_mask, curr_ans = 1, 0
                for i in range(1, n + 1):
                    if (((curr_mask & bitmap) == 0) and (((pos % i) == 0) or ((i % pos) == 0))):
                        curr_ans += dp[1][bitmap | curr_mask]
                    curr_mask <<= 1
                dp[0][bitmap] = curr_ans
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][0]
