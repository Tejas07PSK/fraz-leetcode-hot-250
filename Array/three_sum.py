class Solution:
    def __method1 (self, nums):
        ans, seen_before = set(), set()
        for i in range(len(nums) - 2):
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                if ((target - nums[j]) in seen_before):
                    curr_trip = [nums[i], nums[j], target - nums[j]]
                    curr_trip.sort()
                    ans.add(tuple(curr_trip))
                seen_before.add(nums[j])
            seen_before.clear()
        return list(map(list, ans))

    def __method2 (self, nums):
        nums.sort()
        ans, i = [], 0
        while (i < len(nums) - 2):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while (l < r):
                if ((nums[l] + nums[r]) > target): r -= 1
                elif((nums[l] + nums[r]) < target): l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while (((r - 1) > l) and (nums[r] == nums[r - 1])): r -= 1
                    while (((l + 1) < r) and (nums[l] == nums[l + 1])): l += 1
                    r -= 1
                    l += 1
            while (((i + 1) < (len(nums) - 2)) and (nums[i] == nums[i + 1])): i += 1
            i += 1
        return ans

    def threeSum (self, nums: List[int]) -> List[List[int]]:
        return self.__method2(nums)
        #return self.__method1(nums)
