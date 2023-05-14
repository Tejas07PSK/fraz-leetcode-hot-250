class Solution:
    def __method1 (self, nums):
        curr_min, curr_max, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_max, curr_min = (
                max(curr_max + nums[i], curr_min + nums[i], nums[i]),
                min(curr_max + nums[i], curr_min + nums[i], nums[i])
            )
            ans = max(ans, curr_max)
        return ans

    def __method2 (self, nums):
        curr_max, ans = 0, -10001
        for i in range(len(nums)):
            if ((curr_max + nums[i]) < nums[i]): curr_max = 0
            curr_max += nums[i]
            ans = max(ans, curr_max)
        return ans

    def __method3 (self, l, r, nums):
        if (l == r): return nums[l]
        mid = l + ((r - l) // 2)
        max_from_left = self.__method3(l, mid, nums)
        max_from_right = self.__method3(mid + 1, r, nums)
        curr_max_left, curr_sum = -10001, 0
        for i in range(mid, l - 1, -1):
            curr_sum += nums[i] ; curr_max_left = max(curr_max_left, curr_sum)
        curr_max_right, curr_sum = -10001, 0
        for i in range(mid + 1, r + 1):
            curr_sum += nums[i] ; curr_max_right = max(curr_max_right, curr_sum)
        curr_max = curr_max_left + curr_max_right
        return max(max_from_left, max_from_right, curr_max)

    def maxSubArray (self, nums: List[int]) -> int:
        #return self.__method1(nums)
        return self.__method2(nums)
        # return self.__method3(0, len(nums) - 1, nums)
