class Solution:
    def nextPermutation (self, nums: List[int]) -> None:
        i = len(nums) - 1
        while ((i >= 1) and (nums[i] <= nums[i - 1])): i -= 1
        if (i != 0):
            pivot_ele_idx = i - 1
            while ((i < len(nums)) and (nums[i] > nums[pivot_ele_idx])): i += 1
            nums[pivot_ele_idx], nums[i - 1] = nums[i - 1], nums[pivot_ele_idx]
            i = pivot_ele_idx + 1
        j = len(nums) - 1
        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1 ; j -= 1
