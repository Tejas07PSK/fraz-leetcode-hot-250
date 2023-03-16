class Solution:
    def majorityElement (self, nums: List[int]) -> int:
        cand, freq = nums[0], 1
        for i in range(1, len(nums)):
            if (cand == nums[i]): freq += 1
            else:
                freq -= 1
                if (freq == 0):
                    cand = nums[i]
                    freq = 1
        return cand
