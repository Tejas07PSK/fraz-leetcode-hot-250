class Solution:
    def __method1 (self, i, j, s):
        if (i > j): return 0
        if (i == j): return 1
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = 0
        if (s[i] == s[j]): self.dp[i][j] = 2 + self.__method1(i + 1, j - 1, s)
        self.dp[i][j] = max(self.dp[i][j], self.__method1(i + 1, j, s), self.__method1(i, j - 1, s))
        return self.dp[i][j]

    def __method1_handler (self, s):
        self.dp = [[None for j in range(len(s))] for i in range(len(s))]
        return len(s) - self.__method1(0, len(s) - 1, s)

    def __method2 (self, s):
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                dp[i][j] = 0
                if (s[i] == s[j]): dp[i][j] = 2 + dp[i + 1][j - 1]
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])
        return len(s) - dp[0][-2]

    def __method3 (self, s):
        dp = [[0 for j in range(len(s) + 1)] for i in range(2)]
        for i in range(len(s) - 1, -1, -1):
            dp[0][i] = 1
            for j in range(i + 1, len(s)):
                dp[0][j] = 0
                if (s[i] == s[j]): dp[0][j] = 2 + dp[1][j - 1]
                dp[0][j] = max(dp[0][j], dp[1][j], dp[0][j - 1])
            dp[0], dp[1] = dp[1], dp[0]
        return len(s) - dp[1][-2]

    def minInsertions (self, s: str) -> int:
        #return self.__method1_handler(s)
        #return self.__method2(s)
        return self.__method3(s)
