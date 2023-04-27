class Solution:
    def __method1 (self, i, nums):
        if (i == (len(nums) - 1)):
            self.res.append(list(nums))
            return
        j = i
        while (j < len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.__method1(i + 1, nums)
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    def __method2 (self, size, nums):
        if (size == 1):
            self.res.append(list(nums))
            return
        for i in range(size):
            self.__method2(size - 1, nums)
            if ((size & 1) == 1): nums[0], nums[size - 1] = nums[size - 1], nums[0]
            else: nums[i], nums[size - 1] = nums[size - 1], nums[i]

    def permute (self, nums: List[int]) -> List[List[int]]:
        self.res = []
        #self.__method1(0, nums)
        self.__method2(len(nums), nums)
        return self.res
