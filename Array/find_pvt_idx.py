class Solution:
    def __method1 (self, nums):
        suffix_sum = [0 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1): suffix_sum[i] = nums[i + 1] + suffix_sum[i + 1]
        if (suffix_sum[0] == 0): return 0
        suffix_sum[0] = 0
        for i in range(1, len(nums)):
            if (suffix_sum[i] == (nums[i - 1] + suffix_sum[i - 1])): return i
            suffix_sum[i] = nums[i - 1] + suffix_sum[i - 1]
        return -1

    def __method2 (self, nums):
        tot = sum(nums)
        curr_sum = 0
        for i in range(len(nums)):
            if ((tot - nums[i] - curr_sum) == curr_sum): return i
            curr_sum += nums[i]
        return -1

    def pivotIndex (self, nums: List[int]) -> int:
        return self.__method1(nums)
        #return self.__method2(nums)
