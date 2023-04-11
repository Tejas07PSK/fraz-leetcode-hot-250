class Solution:
    def __method1 (self, nums):
        nums.sort()
        i, j, count = 0, 1, 0
        while (j < len(nums)):
            diff = nums[j] - nums[i]
            if (diff == k):
                count += 1
                while (((j + 1) < len(nums)) and (nums[j] == nums[j + 1])): j += 1
                j += 1
            elif (diff > k): i += 1
            else: j += 1
            if (i == j): j += 1
        return count

    def __method2 (self, nums):
        hm, count = {}, 0
        for num in nums:
            if (num not in hm): hm[num] = 0
            hm[num] += 1
        for key in hm.keys():
            if (((k > 0) and ((key + k) in hm)) or ((k == 0) and (hm[key] > 1))): count += 1
        return count

    def findPairs (self, nums: List[int], k: int) -> int:
        self.__method1(nums)
        # self.__method2(nums)
