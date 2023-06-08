class Solution:
    def __method1 (self, i, j, nums):
        if (i > j): return 0
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = 0 
        left = 1 if ((i - 1) < 0) else nums[i - 1]
        right = 1 if ((j + 1) >= len(nums)) else nums[j + 1]
        k = i
        while (k <= j):
            self.dp[i][j] = max(
                self.dp[i][j],
                (left * nums[k] * right) + self.__method1(i, k - 1, nums) + self.__method1(k + 1, j, nums)
            )
            k += 1
        return self.dp[i][j]

    def __method1_handler (self, nums):
        self.dp = [[None for j in range(len(nums))] for i in range(len(nums))]
        return self.__method1(0, len(nums) - 1, nums)

    def __method2 (self, nums):
        dp = [[0 for j in range(len(nums) + 1)] for i in range(len(nums) + 1)]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                left = 1 if ((i - 1) < 0) else nums[i - 1]
                right = 1 if ((j + 1) >= len(nums)) else nums[j + 1]
                k = i
                while (k <= j):
                    dp[i][j] = max(dp[i][j], ((left * nums[k] * right) + dp[i][k - 1] + dp[k + 1][j]))
                    k += 1
        return dp[0][-2]

    def maxCoins (self, nums: List[int]) -> int:
        #return self.__method1_handler(nums)
        return self.__method2(nums)
