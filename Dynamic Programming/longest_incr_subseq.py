from bisect import bisect_left

class Solution:
    def __method1 (self, i, j, nums):
        if (j == len(nums)): return 0
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.dp[i][j] = 0
        if ((i == j) or (nums[j] > nums[i])): self.dp[i][j] = 1 + self.__method1(j, j + 1, nums)
        self.dp[i][j] = max(self.dp[i][j], self.__method1(i, j + 1, nums))
        self.ans = max(self.ans, self.dp[i][j])
        return self.dp[i][j]

    def __method1_handler (self, nums):
        self.ans, self.dp = 0, [[None for j in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)): self.__method1(i, i, nums)
        return self.ans

    def __method2 (self, nums):
        ans, dp = 0, [[0 for i in range(len(nums))] for j in range(len(nums) + 1)]
        for j in range(len(nums) - 1, -1, -1):
            for i in range(j, -1, -1):
                if ((i == j) or (nums[j] > nums[i])): dp[j][i] = 1 + dp[j + 1][j]
                dp[j][i] = max(dp[j][i], dp[j + 1][i])
                ans = max(ans, dp[j][i])
        return ans

    def __method3 (self, nums):
        ans, dp = 0, [[0 for i in range(len(nums))] for j in range(2)]
        for j in range(len(nums) - 1, -1, -1):
            for i in range(j, -1, -1):
                dp[0][i] = 0
                if ((i == j) or (nums[j] > nums[i])): dp[0][i] = 1 + dp[1][j]
                dp[0][i] = max(dp[0][i], dp[1][i])
                ans = max(ans, dp[0][i])
            dp[0], dp[1] = dp[1], dp[0]
        return ans

    def __method4 (self, nums):
        lis_temp_arr = [nums[0]]
        for i in range(1, len(nums)):
            if (nums[i] > lis_temp_arr[-1]): lis_temp_arr.append(nums[i])
            else: lis_temp_arr[bisect_left(lis_temp_arr, nums[i])] = nums[i]
        return len(lis_temp_arr)

    def __method5 (self, i, nums):
        if (i == len(nums)): return 0
        if (self.dp[i] != None): return self.dp[i]
        self.dp[i] = 1
        for j in range(i + 1, len(nums)):
            if (nums[j] > nums[i]): self.dp[i] = max(self.dp[i], 1 + self.__method5(j, nums))
        self.ans = max(self.ans, self.dp[i])
        return self.dp[i]

    def __method5_handler (self, nums):
        self.ans, self.dp = 0, [None for i in range(len(nums))]
        for i in range(len(nums)): self.__method5(i, nums)
        return self.ans

    def __method6 (self, nums):
        ans, dp = 0, [0 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, len(nums)):
                if (nums[j] > nums[i]): dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        return ans

    def lengthOfLIS (self, nums: List[int]) -> int:
        #return self.__method1_handler(nums)
        #return self.__method2(nums)
        #return self.__method3(nums)
        return self.__method4(nums)
        #return self.__method5_handler(nums)
        #return self.__method6(nums)
