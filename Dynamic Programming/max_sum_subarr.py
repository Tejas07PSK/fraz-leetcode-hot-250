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

    def maxSubArray (self, nums: List[int]) -> int:
        #return self.__method1(nums)
        return self.__method2(nums)
