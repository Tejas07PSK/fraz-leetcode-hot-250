class Solution:
    def __method1 (self, i, j, s):
        if (i > j): return 0
        if (i == j): return 1
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = 0
        if (s[i] == s[j]):
            self.dp[i][j] = (2 * self.__method1(i + 1, j - 1, s)) % self.mod
            left, right = i + 1, j - 1
            while ((left <= right) and (s[left] != s[i])): left += 1
            while ((right >= left) and (s[right] != s[j])): right -= 1
            if (left < right): self.dp[i][j] = (self.dp[i][j] - self.__method1(left + 1, right - 1, s)) % self.mod
            elif (left > right): self.dp[i][j] = (self.dp[i][j] + 2) % self.mod
            else: self.dp[i][j] = (self.dp[i][j] + 1) % self.mod
        else:
            self.dp[i][j] = ((
                (self.__method1(i, j - 1, s) + self.__method1(i + 1, j, s)) % self.mod
            ) - self.__method1(i + 1, j - 1, s)) % self.mod
        return self.dp[i][j]

    def __method1_handler (self, s):
        self.dp = [[None for j in range(len(s))] for i in range(len(s))]
        return self.__method1(0, len(s) - 1, s)

    def __method2 (self, s):
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                dp[i][j] = 0
                if (s[i] == s[j]):
                    dp[i][j] = (2 * dp[i + 1][j - 1]) % self.mod
                    left, right = i + 1, j - 1
                    while ((left <= right) and (s[left] != s[i])): left += 1
                    while ((right >= left) and (s[right] != s[j])): right -= 1
                    if (left < right): dp[i][j] = (dp[i][j] - dp[left + 1][right - 1]) % self.mod
                    elif (left > right): dp[i][j] = (dp[i][j] + 2) % self.mod
                    else: dp[i][j] = (dp[i][j] + 1) % self.mod
                else: dp[i][j] = (((dp[i][j - 1] + dp[i + 1][j]) % self.mod) - dp[i + 1][j - 1]) % self.mod
        return dp[0][-2]

    def countPalindromicSubsequences (self, s: str) -> int:
        self.mod = 1000000007
        #return self.__method1_handler(s)
        return self.__method2(s)
