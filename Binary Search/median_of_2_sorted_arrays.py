class Solution:
    def findMedianSortedArrays (self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if (n2 < n1):
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1
        if (n2 == 0): return ((nums1[(n1 // 2) - 1] + nums1[n1 // 2]) / 2) if ((n1 & 1) == 0) else nums1[n1 // 2]
        left, right = 0, n1 - 1
        half_size = (n1 + n2 + 1) // 2
        while True:
            mid = (left + ((right - left) // 2)) if (left <= right) else (right + ((left - right) // 2))
            left1 = -inf if (mid < 0) else nums1[mid]
            right1 = inf if ((mid + 1) >= n1) else nums1[mid + 1]
            left2 = -inf if ((half_size - mid - 2) < 0) else nums2[half_size - mid - 2]
            right2 = inf if ((half_size - mid - 1) >= n2) else nums2[half_size - mid - 1]
            if ((left1 <= right2) and (left2 <= right1)):
                return ((max(left1, left2) + min(right1, right2)) / 2) if (((n1 + n2) & 1) == 0) else max(left1, left2)
            elif (left1 > right2): right = mid - 1
            else: left = mid + 1
        return 0
