class Solution:
    def __method1 (self, bitmask, target, nums):
        if (self.dp[bitmask] != None): return self.dp[bitmask]
        fltr, self.dp[bitmask] = 1, False
        for i in range(len(nums)):
            if ((fltr & bitmask) > 0):
                if (nums[i] == target):
                    self.dp[bitmask] = (
                        True and
                        self.__method1((bitmask ^ fltr), self.tot_sum, nums)
                    )
                elif (nums[i] < target):
                    self.dp[bitmask] = (
                        self.dp[bitmask] or
                        self.__method1((bitmask ^ fltr), (target - nums[i]), nums)
                    )
                if (self.dp[bitmask]): break
            fltr <<= 1
        return self.dp[bitmask]

    def __method2 (self, target, nums):
        self.sums = [0 for i in range(self.lim)]
        for bitmask in range(1, self.lim):
            fltr, self.dp[bitmask] = 1, False
            for i in range(len(nums)):
                if ((fltr & bitmask) > 0):
                    prev_bitmask = (bitmask ^ fltr)
                    if ((self.sums[prev_bitmask] + nums[i]) == target):
                        self.dp[bitmask] = True and self.dp[prev_bitmask]
                        self.sums[bitmask] = 0
                    elif ((self.sums[prev_bitmask] + nums[i]) < target):
                        self.dp[bitmask] = self.dp[bitmask] or self.dp[prev_bitmask]
                        self.sums[bitmask] = self.sums[prev_bitmask] + nums[i]
                if (self.dp[bitmask]): break
                fltr <<= 1
        return self.dp[-1]

    def __method3 (self, i, fltr, k, bitmask, target, nums):
        res = False
        while (i < len(nums)):
            if ((bitmask & fltr) == 0):
                next_bitmask, next_target = (bitmask | fltr), (target - nums[i])
                if (next_target == 0):
                    next_target = self.tot_sum
                    res = True
                    if ((k - 1) > 1):
                        res = (res and self.__method3(0, 1, k - 1, next_bitmask, next_target, nums))
                elif (next_target > 0):
                    res = (res or self.__method3(i + 1, fltr << 1, k, next_bitmask, next_target, nums))
                if (res == True): break
                if (i == 0): break
                while (((i + 1) < len(nums)) and (nums[i] == nums[i + 1])): fltr, i = fltr << 1, i + 1
            fltr <<= 1 ; i += 1
        return res

    def canPartitionKSubsets (self, nums: List[int], k: int) -> bool:
        self.tot_sum = sum(nums)
        if ((self.tot_sum % k) != 0): return False
        self.tot_sum = (self.tot_sum // k)
        #self.lim = 1 << len(nums)
        #self.dp = [None for i in range(self.lim)]
        #self.dp[0] = True
        nums.sort(reverse=True)
        #return self.__method1((self.lim - 1), self.tot_sum, nums)
        #return self.__method2(self.tot_sum, nums)
        return self.__method3(0, 1, k, 0, self.tot_sum, nums)
