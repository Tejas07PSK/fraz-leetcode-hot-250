class Solution:
    def __method1 (self, i, nums):
        if (i == len(nums)): return 0
        if (self.dp[i] != None): return self.dp[i]
        self.dp[i] = nums[i] ; j = i + 1
        while ((j < len(nums)) and (nums[i] == nums[j])):
            self.dp[i] += nums[j] ; j += 1
        not_take_next_i = j
        while ((j < len(nums)) and (nums[j] == (nums[i] + 1))): j += 1
        self.dp[i] += self.__method1(j, nums)
        self.dp[i] = max(self.dp[i], self.__method1(not_take_next_i, nums))
        return self.dp[i]

    def __method2 (self, nums):
        self.dp[-1] = 0
        for i in range(len(nums) - 1, -1, -1):
            self.dp[i] = nums[i] ; j = i + 1
            while ((j < len(nums)) and (nums[i] == nums[j])):
                self.dp[i] += nums[j] ; j += 1
            not_take_next_i = j
            while ((j < len(nums)) and (nums[j] == (nums[i] + 1))): j += 1
            self.dp[i] += self.dp[j]
            self.dp[i] = max(self.dp[i], self.dp[not_take_next_i])
        return self.dp[0]

    def deleteAndEarn (self, nums: List[int]) -> int:
        nums.sort()
        self.dp = [None for i in range(len(nums) + 1)]
        #return self.__method1(0, nums)
        return self.__method2(nums)
