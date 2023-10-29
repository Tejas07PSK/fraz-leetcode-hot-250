class Solution:
    def __helper (self, cap, nums, maxOperations):
        for i in range(len(nums)):
            ops = nums[i] // cap
            if ((nums[i] % cap) == 0): ops -= 1
            maxOperations -= ops
            if (maxOperations < 0): return False
        return True

    def minimumSize (self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while (left < right):
            mid = left + ((right - left) // 2)
            if (self.__helper(mid, nums, maxOperations)): right = mid
            else: left = mid + 1
        return left
