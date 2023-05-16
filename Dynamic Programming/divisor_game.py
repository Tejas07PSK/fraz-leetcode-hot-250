class Solution:
    def __method1 (self, n):
        if (n == 1): return False
        if (self.dp[n] != None): return self.dp[n]
        self.dp[n] = False
        for i in range(1, n):
            if ((n % i) == 0): self.dp[n] |= (not self.__method1(n - i))
        return self.dp[n]

    def __method2 (self, n):
        self.dp[1] = False
        for i in range(2, n + 1):
            self.dp[i] = False
            for j in range(1, i):
                if ((i % j) == 0): self.dp[i] |= (not self.dp[i - j])
        return self.dp[n]

    def __method3 (self, n): return ((n % 2) == 0)

    def divisorGame (self, n: int) -> bool:
        #self.dp = [None for i in range(n + 1)]
        #return self.__method1(n)
        #return self.__method2(n)
        return self.__method3(n)
