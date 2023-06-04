class Solution:
    def __method1 (self, i, j, word1, word2):
        if (i == len(word1)): return (len(word2) - j)
        if (j == len(word2)): return (len(word1) - i)
        if (self.dp[i][j] != None): return self.dp[i][j]
        if (word1[i] == word2[j]): self.dp[i][j] = self.__method1(i + 1, j + 1, word1, word2)
        else: self.dp[i][j] = 1 + min(
            self.__method1(i + 1, j, word1, word2),
            self.__method1(i, j + 1, word1, word2),
            self.__method1(i + 1, j + 1, word1, word2)
        )
        return self.dp[i][j]

    def __method1_handler (self, word1, word2):
        self.dp = [[None for j in range(len(word2))] for i in range(len(word1))]
        return self.__method1(0, 0, word1, word2)

    def __method2 (self, word1, word2):
        dp = [[None for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(len(word1), -1, -1):
            for j in range(len(word2), -1, -1):
                if (i == len(word1)):
                    dp[i][j] = len(word2) - j
                    continue
                if (j == len(word2)):
                    dp[i][j] = len(word1) - i
                    continue
                if (word1[i] == word2[j]): dp[i][j] = dp[i + 1][j + 1]
                else: dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]

    def __method3 (self, word1, word2):
        dp = [[None for j in range(len(word2) + 1)] for i in range(2)]
        for i in range(len(word1), -1, -1):
            for j in range(len(word2), -1, -1):
                if (i == len(word1)):
                    dp[0][j] = len(word2) - j
                    continue
                if (j == len(word2)):
                    dp[0][j] = len(word1) - i
                    continue
                if (word1[i] == word2[j]): dp[0][j] = dp[1][j + 1]
                else: dp[0][j] = 1 + min(dp[1][j], dp[0][j + 1], dp[1][j + 1])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][0]

    def minDistance (self, word1: str, word2: str) -> int:
        #return self.__method1_handler(word1, word2)
        #return self.__method2(word1, word2)
        return self.__method3(word1, word2)
