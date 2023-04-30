class Solution:
    def __method1 (self, i, n, nums, temp_lst):
        if (i == len(nums)):
            self.res.append(list(temp_lst)) ; return
        temp_lst.append(nums[i]) ; self.__method1(i + 1, n, nums, temp_lst) ; temp_lst.pop()
        while (((i + 1) < len(nums)) and (nums[i + 1] == nums[i])): i += 1
        self.__method1(i + 1, n, nums, temp_lst)

    def __subsetsWithDupHelper1 (self, nums):
        self.res = []
        self.__method1(0, len(nums), nums, [])
        return self.res

    def __subsetsWithDupHelper2 (self, nums):
        self.res = set()
        for i in range(2 ** len(nums)):
            idx, temp_res, bit_map = 0, [], i
            while (bit_map > 0):
                if ((bit_map & 1) > 0): temp_res.append(nums[idx])
                bit_map >>= 1 ; idx += 1
            self.res.add(tuple(temp_res))
            del temp_res
        self.res = list(map(list, self.res))
        return self.res

    def subsetsWithDup (self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #return self.__subsetsWithDupHelper1(nums)
        return self.__subsetsWithDupHelper2(nums)
