class Solution:
    def checkSubarraySum (self, nums: List[int], k: int) -> bool:
        hm, curr_prefix_sum = {}, 0
        for i in range(len(nums)):
            curr_prefix_sum += nums[i]
            curr_rem = curr_prefix_sum % k
            if ((curr_rem == 0) and (i >= 1)): return True
            if (curr_rem not in hm): hm[curr_rem] = i + 1
            elif  (hm[curr_rem] < i): return True
        return False
