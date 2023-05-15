class Solution:
    def __method1 (self, n):
        if (n == -1): return 0
        if (n == 0): return 1
        if (self.dp[n] != None): return self.dp[n]
        self.dp[n] = self.__method1(n - 1) + self.__method1(n - 2)
        return self.dp[n]

    def __method2 (self, n):
        self.dp[0], self.dp[1] = 1, 1
        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]

    def __method3 (self, n):
        prev1, prev2 = 1, 1
        for i in range(2, n + 1):
            temp = prev1 + prev2
            prev1, prev2 = temp, prev1
        return prev1

    def climbStairs (self, n: int) -> int:
        self.dp = [None for i in range(n + 1)]
        #return self.__method1(n)
        #return self.__method2(n)
        return self.__method3(n)
