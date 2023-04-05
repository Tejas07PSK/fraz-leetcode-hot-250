class Solution:
    def jump (self, nums: List[int]) -> int:
        i, jumps = 0, 0
        while (i < (len(nums) - 1)):
            if ((nums[i]) == 0): return -1
            jumps += 1
            if ((nums[i] + i) >= (len(nums) - 1)): return jumps
            max_end, j, next_i = nums[i] + i, i + 1, nums[i] + i
            while (j <= (nums[i] + i)):
                if ((nums[j] != 0) and ((nums[j] + j) > max_end)):
                    max_end = nums[j] + j
                    next_i = j
                j += 1
            i = next_i
        return jumps
