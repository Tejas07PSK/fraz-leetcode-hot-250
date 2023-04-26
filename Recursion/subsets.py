class Solution:
    def __method1 (self, i, nums, curr_res):
        if (i == len(nums)):
            self.res.append(list(curr_res))
            return
        curr_res.append(nums[i]) ; self.__method1(i + 1, nums, curr_res)
        curr_res.pop() ; self.__method1(i + 1, nums, curr_res)

    def __method2 (self, nums):
        for i in range(2 ** len(nums)):
            idx, bin_num, curr_res = 0, i, []
            while (bin_num > 0):
                if ((bin_num & 1) > 0): curr_res.append(nums[idx])
                bin_num >>= 1 ; idx += 1
            self.res.append(curr_res)

    def subsets (self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.__method1(0, nums, deque())
        #self.__method2(nums)
        return self.res
