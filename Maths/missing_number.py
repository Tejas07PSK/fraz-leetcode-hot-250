class Solution:
    def __method1 (self, nums):
        act_sum = len(nums) * (len(nums) + 1) // 2
        given_sum = sum(nums)
        return act_sum - given_sum

    def __method2 (self, nums):
        i = 0
        while (i < len(nums)):
            if ((nums[i] == len(nums)) or (nums[i] == i)): i += 1
            else:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        i = 0
        while (i < len(nums)):
            if (i != nums[i]): return i
            i += 1
        return i

    def __method3 (self, nums):
        xor = 0
        for i in range(len(nums)): xor ^= nums[i]
        for i in range(len(nums) + 1): xor ^= i
        return xor

    def missingNumber (self, nums: List[int]) -> int:
        #return self.__method1(nums)
        return self.__method2(nums)
        #return self.__method3(nums)
