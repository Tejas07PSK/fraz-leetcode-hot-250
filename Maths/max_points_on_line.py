from collections import defaultdict

class Solution:
    def __gcd (self, a, b):
        while (b):
            a = a % b
            a, b = b, a
        return a

    def maxPoints (self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            hm, dups = defaultdict(int), 1
            for j in range(i + 1, len(points)):
                if ((points[i][0] == points[j][0]) and (points[i][1] == points[j][1])):
                    dups += 1
                else:
                    dy = points[j][1] - points[i][1]
                    dx = points[j][0] - points[i][0]
                    g = self.__gcd(dx, dy)
                    hm[str(dx // g) + '_' + str(dy // g)] += 1
            ans = max(ans, dups)
            for value in hm.values(): ans = max(ans, value + dups)
            del hm
        return ans
