class Solution:
    def subarraysDivByK (self, nums: List[int], k: int) -> int:
        hm, count, curr_sum = {0:0}, 0, 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            curr_rem = curr_sum % k
            if (curr_rem == 0): count += 1
            if (curr_rem in hm):
                count += hm[curr_rem]
                hm[curr_rem] += 1
            else: hm[curr_rem] = 1
        return count
