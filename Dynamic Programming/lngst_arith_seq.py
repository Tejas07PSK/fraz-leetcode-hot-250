class Solution:
    def __method1 (self, nums):
        dp, ans = {}, 0
        for i in range(len(nums) - 1, -1, -1):
            dp[(i, 0)] = 1
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if ((i, diff) not in dp): dp[(i, diff)] = 0
                dp[(i, diff)] = max(dp[(i, diff)], dp.get((j, diff), 1) + 1)
                ans = max(ans, dp[(i, diff)])
        return ans

    def __method2 (self, nums):
        dp, ans = {}, 0
        for j in range(len(nums)):
            for i in range(j):
                diff = nums[j] - nums[i]
                dp[(j, diff)] = dp.get((i, diff), 1) + 1
                ans = max(ans, dp[(j, diff)])
        return ans

    def __method3 (self, nums):
        dp, valid_nums, ans = {}, set(), 0
        for num in nums:
            for prev_num in valid_nums:
                diff = num - prev_num
                dp[(num, diff)] = dp.get((prev_num, diff), 1) + 1
                ans = max(ans, dp[(num, diff)])
            valid_nums.add(num)
        return ans

    def longestArithSeqLength (self, nums: List[int]) -> int:
        #return self.__method1(nums)
        #return self.__method2(nums)
        return self.__method3(nums)
