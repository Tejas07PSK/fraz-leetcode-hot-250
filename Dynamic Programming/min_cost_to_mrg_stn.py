from math import inf

class Solution:
    def __method1 (self, i, j, k):
        if (i >= j): return 0
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = inf
        for l in range(i, j + 1, k - 1):
            self.dp[i][j] = min(
                self.dp[i][j],
                self.__method1(i, l, k) + self.__method1(l + 1, j, k)
            )
        if (((j - i) % (k - 1)) == 0):
            self.dp[i][j] += (self.prefix_sum[j + 1] - self.prefix_sum[i])
        return self.dp[i][j]

    def __method1_handler (self, stones, k):
        self.dp = [[None for j in range(len(stones))] for i in range(len(stones))]
        return self.__method1(0, len(stones) - 1, k)

    def __method2 (self, stones, k):
        dp = [[(0 if (i >= j) else inf) for j in range(len(stones) + 1)] for i in range(len(stones) + 1)]
        for i in range(len(stones) - 1, -1, -1):
            for j in range(i + 1, len(stones)):
                dp[i][j] = inf
                for l in range(i, j + 1, k - 1): dp[i][j] = min(dp[i][j], (dp[i][l] + dp[l + 1][j]))
                if (((j - i) % (k - 1)) == 0): dp[i][j] += (self.prefix_sum[j + 1] - self.prefix_sum[i])
        return dp[0][-2]

    def mergeStones (self, stones: List[int], k: int) -> int:
        if (((len(stones) - 1) % (k - 1)) != 0): return -1
        self.prefix_sum = [0 for i in range(len(stones) + 1)]
        for i in range(1, len(stones) + 1): self.prefix_sum[i] = self.prefix_sum[i - 1] + stones[i - 1]
        #return self.__method1_handler(stones, k)
        return self.__method2(stones, k)
