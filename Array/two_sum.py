class Solution:
    def __method1 (self, nums, target):
        seen_before = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in seen_before):
                return [seen_before[target - nums[i]], i]
            if (nums[i] not in seen_before): seen_before[nums[i]] = i
        return [-1, -1]

    def __method2 (self, nums, target):
        nums = list(enumerate(nums)) ; nums.sort(key = lambda x: x[1])
        i, j = 0, len(nums) - 1
        while (i < j):
            if ((nums[i][1] + nums[j][1]) == target): return [nums[i][0], nums[j][0]]
            elif ((nums[i][1] + nums[j][1]) > target): j -= 1
            else: i += 1
        return [-1, -1]

    def twoSum (self, nums: List[int], target: int) -> List[int]:
        return self.__method1(nums, target)
        #return self.__method2(nums, target)
