class Solution:
    def maxProduct (self, nums: List[int]) -> int:
        curr_max, curr_min, glob_max = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_max, curr_min = max(curr_max * nums[i], curr_min * nums[i], nums[i]), min(curr_max * nums[i], curr_min * nums[i], nums[i])
            glob_max = max(glob_max, curr_max)
        return glob_max
