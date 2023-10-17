class Solution:
    def mySqrt(self, x: int) -> int:
        if ((x == 0) or (x == 1)):
            return x
        left, right = 0, x // 2
        res = 0
        while (left <= right):
            mid = left + ((right - left) // 2)
            pwr = mid * mid
            if (pwr == x):
                return mid
            elif (pwr < x):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
