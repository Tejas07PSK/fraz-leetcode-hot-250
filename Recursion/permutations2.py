class Solution:
    def __method1 (self, size, nums):
        if (size == 1):
          self.res.add(tuple(nums))
          return
        for i in range(size):
          self.__method1(size - 1, nums)
          if ((size & 1) == 1): nums[0], nums[size - 1] = nums[size - 1], nums[0]
          else: nums[i], nums[size - 1] = nums[size - 1], nums[i]

    def __method2 (self, i, num_freq_hm, unq_nums, size, nums):
        for num in unq_nums:
          if (num_freq_hm[num] > 0):
            tmp = nums[i] ; nums[i] = num
            if (i < (size - 1)):
              num_freq_hm[num] -= 1
              self.__method2(i + 1, num_freq_hm, unq_nums, size, nums)
              num_freq_hm[num] += 1
            else: self.res.append(list(nums))
            nums[i] = tmp

    def __method1_handler (self, nums):
        self.res = set() ; self.__method1(len(nums), nums)
        return list(map(list, self.res))

    def __method2_handler (self, nums):
        self.res, num_freq_hm, unq_nums = [], {}, []
        for num in nums:
          if (num not in num_freq_hm):
            unq_nums.append(num) ; num_freq_hm[num] = 0
          num_freq_hm[num] += 1
        self.__method2(0, num_freq_hm, unq_nums, len(nums), nums)
        return self.res

    def permuteUnique (self, nums: List[int]) -> List[List[int]]:
        #return self.__method1_handler(nums)
        return self.__method2_handler(nums)
