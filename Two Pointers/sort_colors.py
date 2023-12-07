class Solution:
    def sortColors (self, nums: List[int]) -> None:
        i, j, k, n = 0, 0, len(nums) - 1, len(nums)
        while (i <= k):
            if (nums[i] == 0):
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            elif (nums[i] == 1): i += 1
            else:
                nums[k], nums[i] = nums[i], nums[k]
                k -= 1
        return nums
