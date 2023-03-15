class Solution:
    def __method1 (self, nums):
        last_zero_idx = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                if (i != last_zero_idx): nums[i], nums[last_zero_idx] = 0, nums[i]
                last_zero_idx += 1
        return nums

    def __method2 (self, nums):
        last_zero_idx = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                if (i != last_zero_idx): nums[last_zero_idx] = nums[i]
                last_zero_idx += 1
        for i in range(last_zero_idx, len(nums)): nums[i] = 0
        return nums

    def moveZeroes (self, nums: List[int]) -> None:
        return self.__method1(nums)
        #return self.__method2(nums)
