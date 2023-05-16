class Solution:
    def __method1 (self, n):
        if (self.dp[n] != None): return self.dp[n]
        self.dp[n] = self.__method1(n // 2)
        if ((n % 2) == 1): self.dp[n] += 1
        self.__method1(n - 1)
        return self.dp[n]

    def __method2 (self, n):
        for i in range(1, n + 1):
            self.dp[i] = self.dp[i // 2]
            if ((i % 2) == 1): self.dp[i] += 1

    def countBits(self, n: int) -> List[int]:
        self.dp = [None for i in range(n + 1)] ; self.dp[0] = 0
        #self.__method1(n)
        self.__method2(n)
        return self.dp
