class Solution:
    def __method1 (self, size, nums):
        if (size == 1):
            self.res.add(tuple(nums))
            return
        for i in range(size):
            self.__method1(size - 1, nums)
            if ((size & 1) == 1): nums[0], nums[size - 1] = nums[size - 1], nums[0]
            else: nums[i], nums[size - 1] = nums[size - 1], nums[i]

    def __method1_handler(self, nums):
        self.res = set() ; self.__method1(len(nums), nums)
        return list(map(list, self.res))

    def permuteUnique (self, nums: List[int]) -> List[List[int]]:
        return self.__method1_handler(nums)
