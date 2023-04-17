class Solution:
    def canJump (self, nums: List[int]) -> bool:
        prev_max_jump, i = 0, 0
        while (i < (len(nums) - 1)):
            if (nums[i] == 0): return False
            if ((i + nums[i]) >= (len(nums) - 1)): return True
            next_i = i + nums[i]
            max_jump = next_i + nums[next_i]
            j = next_i - 1
            while (j > prev_max_jump):
                if ((j + nums[j]) > max_jump): max_jump, next_i = j + nums[j], j
                j -= 1
            prev_max_jump = i + nums[i]
            i = next_i
        return True
