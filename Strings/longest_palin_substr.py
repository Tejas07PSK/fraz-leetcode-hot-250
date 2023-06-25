class Solution:
    def __method1 (self, i, j, s):
        if (i == j): return 1
        if (i > j): return 0
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = -1
        if (s[i] == s[j]):
            inner_sub_str = self.__method1(i + 1, j - 1, s)
            if (inner_sub_str != -1):
                self.dp[i][j] = 2 + inner_sub_str
            if (self.dp[i][j] > self.ans[0]): self.ans[0], self.ans[1], self.ans[2] = self.dp[i][j], i, j
        self.__method1(i + 1, j, s)
        self.__method1(i, j - 1, s)
        return self.dp[i][j]

    def __method1_handler (self, s):
        self.ans, self.dp = [0, 0, 0], [[None for j in range(len(s))] for i in range(len(s))]
        self.__method1(0, len(s) - 1, s)
        return s[self.ans[1]:self.ans[2]+1]

    def __method2 (self, s):
        ans, dp = [0, 0, 0], [[0 for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                dp[i][j] = -1
                if (s[i] != s[j]): continue
                inner_sub_str = dp[i + 1][j - 1]
                if (inner_sub_str != -1): dp[i][j] = 2 + dp[i + 1][j - 1]
                if (dp[i][j] > ans[0]): ans[0], ans[1], ans[2] = dp[i][j], i, j
        return s[ans[1]:ans[2]+1]

    def __method3 (self, s):
        ans, dp = [0, 0, 0], [[0 for j in range(len(s))] for i in range(2)]
        for i in range(len(s) - 1, -1, -1):
            dp[0][i] = 1
            for j in range(i + 1, len(s)):
                dp[0][j] = -1
                if (s[i] != s[j]): continue
                inner_sub_str = dp[1][j - 1]
                if (inner_sub_str != -1): dp[0][j] = 2 + inner_sub_str
                if (dp[0][j] > ans[0]): ans[0], ans[1], ans[2] = dp[0][j], i, j
            dp[0], dp[1] = dp[1], dp[0]
        return s[ans[1]:ans[2]+1]

    def __method4_helper (self, left, right, size, n, s):
        while ((left >= 0) and (right < n) and (s[left] == s[right])):
            left -= 1 ; right += 1 ; size += 2
        return left + 1, right - 1, size

    def __method4 (self, s):
        ans, n = [0, 0, 0], len(s)
        for i in range(n):
            left, right, size = self.__method4_helper(i - 1, i + 1, 1, n, s)
            if (size > ans[0]): ans[0], ans[1], ans[2] = size, left, right
            left, right, size = self.__method4_helper(i, i + 1, 0, n, s)
            if (size > ans[0]): ans[0], ans[1], ans[2] = size, left, right
        return s[ans[1]:ans[2]+1]

    def longestPalindrome (self, s: str) -> str:
        return self.__method4(s)
        #return self.__method3(s)
        #return self.__method2(s)
        #return self.__method1_handler(s)
