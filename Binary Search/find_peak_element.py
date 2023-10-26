from math import inf

class Solution:
    def findPeakElement (self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = left + ((right - left) // 2)
            curr = nums[mid]
            nxt = nums[mid + 1] if ((mid + 1) < len(nums)) else -inf
            prev = nums[mid - 1] if ((mid - 1) >= 0) else -inf
            if (prev < curr > nxt): return mid
            elif (prev > curr > nxt): right = mid - 1
            elif (prev < curr < nxt): left = mid + 1
            else: left = mid + 1
        return -1
