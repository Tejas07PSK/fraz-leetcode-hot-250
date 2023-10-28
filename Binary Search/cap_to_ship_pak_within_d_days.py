class Solution:
    def __helper (self, capacity, days, weights):
        cap, i = capacity, 0
        while (i < len(weights)):
            wt = weights[i]
            if ((cap - wt) < 0):
                days -= 1
                if (days == 0): return False
                cap = capacity
                continue
            else:
                cap -= wt
                i += 1
        return True

    def shipWithinDays (self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while (left < right):
            mid = left + ((right - left) // 2)
            res = self.__helper(mid, days, weights)
            if (res): right = mid
            else: left = mid + 1
        return left
