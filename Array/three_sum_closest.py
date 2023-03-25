from math import inf
class Solution:
    def threeSumClosest (self, nums: List[int], target: int) -> int:
        glob_min_diff, ans = inf, None
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while (j < k):
                curr_sum = nums[i] + nums[j] + nums[k]
                if (curr_sum == target): return curr_sum
                curr_diff = abs(target - curr_sum)
                if (curr_diff < glob_min_diff):
                    glob_min_diff = curr_diff
                    ans = curr_sum
                if (curr_sum > target): k -= 1
                else: j += 1
        return ans
