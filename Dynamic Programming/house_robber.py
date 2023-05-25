class Solution:
    def rob (self, nums: List[int]) -> int:
        next_1, next_2 = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            temp = nums[i] + next_2
            temp = max(temp, next_1)
            next_2 = next_1
            next_1 = temp
        return next_1
