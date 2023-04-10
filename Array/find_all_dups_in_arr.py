class Solution:
    def findDuplicates (self, nums: List[int]) -> List[int]:
        i = 0
        while (i < len(nums)):
            if (nums[i] == nums[nums[i] - 1]): i += 1
            else:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        res, i = [], 0
        while (i < len(nums)):
            if (nums[i] != (i + 1)): res.append(nums[i])
            i += 1
        return res
