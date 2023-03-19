class Solution:
    def subarraySum (self, nums: List[int], k: int) -> int:
        seen_before, curr_sum, ans = {}, 0, 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum == k): ans += 1
            if ((curr_sum - k) in seen_before): ans += seen_before[curr_sum - k]
            if (curr_sum not in seen_before): seen_before[curr_sum] = 0
            seen_before[curr_sum] += 1
        return ans
