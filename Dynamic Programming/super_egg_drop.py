from math import inf

class Solution:
    def __method1 (self, k, n):
        if ((k == 0) or (n == 0)): return 0
        if (k == 1): return n
        if (n == 1): return 1
        if (self.dp[k][n] != None): return self.dp[k][n]
        self.dp[k][n] = inf
        for i in range(1, n + 1):
            self.dp[k][n] = min(self.dp[k][n], max(self.__method1(k - 1, i - 1), self.__method1(k, n - i)))
        self.dp[k][n] += 1
        return self.dp[k][n]

    def __method1_helper (self, k, n):
        self.dp = [[None for j in range(n + 1)] for i in range(k + 1)]
        return self.__method1(k, n)

    def __method2 (self, k, n):
        dp = [[0 for j in range(n + 1)] for i in range(k + 1)]
        for i in range(k + 1):
            for j in range(n + 1):
                if ((i == 0) or (j == 0)):
                    dp[i][j] = 0 ; continue
                if (i == 1):
                    dp[i][j] = j ; continue
                if (j == 1):
                    dp[i][j] = 1 ; continue
                dp[i][j] = inf
                for l in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][l - 1], dp[i][j - l]))
                dp[i][j] += 1
        return dp[-1][-1]

    def __method3 (self, k, n):
        dp = [[0 for j in range(n + 1)] for i in range(2)]
        for i in range(k + 1):
            for j in range(n + 1):
                if ((i == 0) or (j == 0)):
                    dp[1][j] = 0 ; continue
                if (i == 1):
                    dp[1][j] = j ; continue
                if (j == 1):
                    dp[1][j] = 1 ; continue
                dp[1][j] = inf
                for l in range(1, j + 1):
                    dp[1][j] = min(dp[1][j], max(dp[0][l - 1], dp[1][j - l]))
                dp[1][j] += 1
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][-1]

    def __method4_bino_coeff_helper (self, drops, k, n):
        ans, f = 0, 1
        for i in range(1, k + 1):
            f *= drops - i + 1
            f //= i
            ans += f
            if (ans >= n): break
        return ans
    
    def __method4 (self, k, n):
        low, high = 1, n
        while (low < high):
            mid = low + ((high - low) // 2)
            if (self.__method4_bino_coeff_helper(mid, k, n) < n): low = mid + 1
            else: high = mid
        return low

    def superEggDrop (self, k: int, n: int) -> int:
        #return self.__method1_helper(k, n)
        #return self.__method2(k, n)
        #return self.__method3(k, n)
        return self.__method4(k, n)
