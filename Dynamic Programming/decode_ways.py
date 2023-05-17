class Solution:
    def __method1 (self, i, s, n):
        if (self.dp[i] != None): return self.dp[i]
        self.dp[i] = 0
        if (s[i] == '0'): return self.dp[i]
        if (1 <= int(s[i]) <= 9):
            if ((i + 1) >= n): self.dp[i] += 1
            else: self.dp[i] += self.__method1(i + 1, s, n)
        if (10 <= int(s[i:i + 2]) <= 26):
            if ((i + 2) >= n): self.dp[i] += 1
            else: self.dp[i] += self.__method1(i + 2, s, n)
        return self.dp[i]

    def __method2 (self, s, n):
        for i in range(n - 1, -1, -1):
            self.dp[i] = 0
            if (s[i] == '0'): continue
            if (1 <= int(s[i]) <= 9):
                if ((i + 1) >= n): self.dp[i] += 1
                else: self.dp[i] += self.dp[i + 1]
            if (10 <= int(s[i:i + 2]) <= 26):
                if ((i + 2) >= n): self.dp[i] += 1
                else: self.dp[i] += self.dp[i + 2]
        return self.dp[0]

    def numDecodings (self, s: str) -> int:
        self.dp = [None for i in range(len(s))]
        #return self.__method1(0, s, len(s))
        return self.__method2(s, len(s))
