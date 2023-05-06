class Solution:
    def __canPartitionKSubsetsHelper (self, k, bitmask, target, nums):
        if (self.dp[bitmask] != None): return self.dp[bitmask]
        fltr, self.dp[bitmask] = 1, False
        for i in range(len(nums)):
            if ((bitmask & fltr) == 0):
                next_bitmask, next_target = (bitmask | fltr), (target - nums[i])
                if (next_target == 0):
                    next_target = self.tot_sum
                    self.dp[bitmask] = True
                    if ((k - 1) > 1):
                        self.dp[bitmask] = (self.dp[bitmask] and self.__canPartitionKSubsetsHelper(k - 1, next_bitmask, next_target, nums))
                elif (next_target > 0):
                    self.dp[bitmask] = (self.dp[bitmask] or self.__canPartitionKSubsetsHelper(k, next_bitmask, next_target, nums))
            if (self.dp[bitmask]): break
            fltr <<= 1
        return self.dp[bitmask]

    def canPartitionKSubsets (self, nums: List[int], k: int) -> bool:
        self.tot_sum = sum(nums)
        if ((self.tot_sum % k) != 0): return False
        self.tot_sum, self.dp = (self.tot_sum // k), [None for i in range(1 << len(nums))]
        nums.sort(reverse=True)
        return self.__canPartitionKSubsetsHelper(k, 0, self.tot_sum, nums)
        
