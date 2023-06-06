from math import inf

class Solution:
    def __method1 (self, i, d, jobDifficulty):
        if (d == 0): return 0 if (i == len(jobDifficulty)) else -1
        if (self.dp[i][d] != None): return self.dp[i][d]
        curr_max, ans = -1, inf
        for j in range(i, len(jobDifficulty) - d + 1):
            curr_max = max(curr_max, jobDifficulty[j])
            next_half = self.__method1(j + 1, d - 1, jobDifficulty)
            if (next_half != -1): ans = min(ans, (curr_max + next_half))
        self.dp[i][d] = ans if (ans != inf) else -1
        return self.dp[i][d]

    def __method1_handler (self, jobDifficulty, d):
        self.dp = [[None for j in range(d + 1)] for i in range(len(jobDifficulty))]
        return self.__method1(0, d, jobDifficulty)

    def __method2 (self, jobDifficulty, days):
        dp = [[-1 for j in range(len(jobDifficulty) + 1)] for i in range(days + 1)]
        dp[0][-1] = 0
        for d in range(1, days + 1):
            for i in range(len(jobDifficulty) - 1, -1, -1):
                curr_max, ans, dp[d][i] = -1, inf, -1
                for j in range(i, len(jobDifficulty) - d + 1):
                    curr_max = max(curr_max, jobDifficulty[j])
                    next_half = dp[d - 1][j + 1]
                    if (next_half != -1): ans = min(ans, (curr_max + next_half))
                if (ans != inf): dp[d][i] = ans
        return dp[days][0]

    def __method3 (self, jobDifficulty, days):
        dp = [[-1 for j in range(len(jobDifficulty) + 1)] for i in range(2)]
        dp[0][-1] = 0
        for d in range(1, days + 1):
            for i in range(len(jobDifficulty) - 1, -1, -1):
                curr_max, ans, dp[1][i] = -1, inf, -1
                for j in range(i, len(jobDifficulty) - d + 1):
                    curr_max = max(curr_max, jobDifficulty[j])
                    next_half = dp[0][j + 1]
                    if (next_half != -1): ans = min(ans, (curr_max + next_half))
                if (ans != inf): dp[1][i] = ans
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][0]

    def minDifficulty (self, jobDifficulty: List[int], d: int) -> int:
        #return self.__method1_handler(jobDifficulty, d)
        #return self.__method2(jobDifficulty, d)
        return self.__method3(jobDifficulty, d)
