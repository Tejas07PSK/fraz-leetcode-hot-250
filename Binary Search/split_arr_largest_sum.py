class Solution:
    def __helper (self, nums, cap, lim):
        tot = 0
        for num in nums:
            tot += num
            if (tot > cap):
                tot = num
                lim -= 1
                if (lim == 0): return False
        return True

    def splitArray (self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while (left < right):
            mid  = left + (right - left) // 2
            if (self.__helper(nums, mid, k)): right = mid
            else: left = mid + 1
        return left
