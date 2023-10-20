from math import inf
class Solution:
    def peakIndexInMountainArray (self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while (left <= right):
            mid = left + ((right - left) // 2)
            curr = arr[mid]
            prev = -inf if ((mid - 1) < 0) else arr[mid - 1]
            nxt = -inf if ((mid + 1) >= len(arr)) else arr[mid + 1]
            if (prev <= curr >= nxt): return mid
            elif (nxt <= curr <= prev): right = mid - 1
            elif  (prev <= curr <= nxt): left = mid + 1
        return -1
