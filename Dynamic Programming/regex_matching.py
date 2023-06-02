class Solution:
    def __method1 (self, i, j, s, p):
        if (i == len(s)):
            if (((len(p) - j) % 2) == 1): return False
            while (j < (len(p) - 1)):
                if (p[j + 1] != '*'): return False
                j += 2
            return True
        if (j == len(p)): return (i == len(s))
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = False
        if (p[j] == '.'):
            if (97 <= ord(s[i]) <= 122): self.dp[i][j] = True
        else:
            if (p[j] == s[i]): self.dp[i][j] = True
        if (((j + 1) < len(p)) and (p[j + 1] == '*')):
            self.dp[i][j] = self.dp[i][j] and self.__method1(i + 1, j, s, p) or self.__method1(i, j + 2, s, p)
        else:
            self.dp[i][j] = self.dp[i][j] and self.__method1(i + 1, j + 1, s, p)
        return self.dp[i][j]

    def __method1_handler (self, s, p):
        self.dp = [[None for j in range(len(p))] for i in range(len(s))]
        return self.__method1(0, 0, s, p)

    def __method2 (self, s, p):
        dp = [[None for j in range(len(p) + 1)] for i in range(2)]
        dp[1][-1] = True
        for j in range(len(p) - 1, -1, -1):
            if (p[j] == '*'): continue
            if (((len(p) - j) % 2) == 1):
                dp[1][j] = False
                continue
            dp[1][j] = ((p[j + 1] == '*') and dp[1][j + 2])
        for i in range(len(s) - 1, -1, -1):
            dp[0][-1] = False
            for j in range(len(p) - 1, -1, -1):
                dp[0][j] = False
                if (p[j] == '.'):
                    if (97 <= ord(s[i]) <= 122): dp[0][j] = True
                else:
                    if (p[j] == s[i]): dp[0][j] = True
                if (((j + 1) < len(p)) and (p[j + 1] == '*')):
                    dp[0][j] = dp[0][j] and dp[1][j] or dp[0][j + 2]
                else:
                    dp[0][j] = dp[0][j] and dp[1][j + 1]
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][0]

    def isMatch (self, s: str, p: str) -> bool:
        #return self.__method1_handler(s, p)
        return self.__method2(s, p)
