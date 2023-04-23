from math import inf
from heapq import heappush, heappop
from collections import deque

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

    def __method2 (points, k):
        hp, ans = [], -inf
        for i in range(len(points)):
            while (hp and ((points[i][0] - hp[0][1]) > k)): heappop(hp)
            if hp: ans = max(ans, (-hp[0][0] + points[i][0] + points[i][1]))
            heappush(hp, ((points[i][0] - points[i][1]), points[i][0]))
        return ans

    def __method3 (points, k):
        dq, ans = deque(), -inf
        for i in range(len(points)):
            while (dq and ((points[i][0] - dq[0][1]) > k)): dq.popleft()
            if dq: ans = max(ans, (dq[0][0] + points[i][0] + points[i][1]))
            while (dq and (dq[-1][0] < (points[i][1] - points[i][0]))): dq.pop()
            dq.append(((points[i][1] - points[i][0]), points[i][0]))
        return ans

    def findMaxValueOfEquation (self, points: List[List[int]], k: int) -> int:
        return self.__method1(points, k)
        # return self.__method2(points, k)
        # return self.__method3(points, k)
