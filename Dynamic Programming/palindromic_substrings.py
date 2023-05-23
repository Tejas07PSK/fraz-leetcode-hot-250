class Solution:
    def __method1 (self, s):
        dp, ans = [[True for j in range(len(s) + 1)] for i in range(2)], 0
        for i in range(len(s) - 1, -1, -1):
            dp[0][i] = True
            ans += 1
            for j in range(i + 1, len(s)):
                dp[0][j] = ((s[i] == s[j]) and dp[1][j - 1])
                if (dp[0][j]): ans += 1
            dp[0], dp[1] = dp[1], dp[0]
        return ans

    def __method2 (self, s):
        ans = 0
        for i in range(len(s)):
           x, y = i, i
           while ((x >= 0) and (y < len(s)) and (s[x] == s[y])):
               x -= 1 ; y += 1 ; ans += 1
           x, y = i, i + 1
           while ((x >= 0) and (y < len(s)) and (s[x] == s[y])):
               x -= 1 ; y += 1 ; ans += 1
        return ans

    def countSubstrings(self, s: str) -> int:
        #return self.__method1(s)
        return self.__method2(s)
