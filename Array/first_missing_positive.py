class Solution:
    def __method1 (self, nums):
        mx_val = len(nums) + 1
        for i in range(len(nums)):
            if ((nums[i] <= 0) or (nums[i] > len(nums))): nums[i] = 0
        for i in range(len(nums)):
            if ((nums[i] != 0) and ((nums[(nums[i] % mx_val) - 1] // mx_val) != (nums[i] % mx_val))):
                nums[(nums[i] % mx_val) - 1] += (nums[i] % mx_val) * mx_val
        for i in range(len(nums)):
            if ((i + 1) != (nums[i] // mx_val)): return i + 1
        return len(nums) + 1

    def __method2 (self, nums):
        mx_val = len(nums) + 1
        for i in range(len(nums)):
            if ((nums[i] <= 0) or (nums[i] > len(nums))): nums[i] = 0
        for i in range(len(nums)):
            if (nums[i] != 0): nums[(nums[i] % mx_val) - 1] += mx_val
        for i in range(len(nums)):
            if ((nums[i] // mx_val) == 0): return i + 1
        return len(nums) + 1

    def __method3 (self, nums):
        i = 0
        while (i < len(nums)):
            if (0 < nums[i] <= len(nums)):
                if (nums[nums[i] - 1] != nums[i]):
                    temp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = temp
                else: i += 1
            else: i += 1
        i = 0
        for i in range(len(nums)):
            if ((i + 1) != nums[i]): return i + 1
        return len(nums) + 1

    def firstMissingPositive (self, nums: List[int]) -> int:
        return self.__method3(nums)
        #return self.__method1(nums)
        #return self.__method2(nums)
