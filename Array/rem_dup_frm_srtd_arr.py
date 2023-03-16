class Solution:
    def removeDuplicates (self, nums: List[int]) -> int:
        k, i = 0, 0
        while (i < len(nums)):
            while (((i + 1) < len(nums)) and (nums[i] == nums[i + 1])): i += 1
            nums[k] = nums[i]
            k += 1 ; i += 1
        return k
