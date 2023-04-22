from math import inf
class Solution:
    def __method1 (points, k):
        i, j, ans = 0, 1, -inf
        while (j < len(points)):
            diff = points[j][0] - points[i][0]
            if (diff <= k):
                ans = max(ans, (points[i][1] + points[j][1] + diff))
                if ((j == len(points) - 1) or ((points[i][1] + diff) <= points[j][1])): i += 1
                else: j += 1
            else: i += 1
            if (i == j): j += 1
        return ans

    def findMaxValueOfEquation (self, points: List[List[int]], k: int) -> int:
        return self.__method1(points, k)