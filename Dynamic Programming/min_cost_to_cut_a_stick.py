from math import inf
class Solution:
    def __method1 (self, left, right, cuts):
        if ((left + 1) == right): return 0
        if (self.dp[left][right] != None): return self.dp[left][right]
        self.dp[left][right] = inf
        for i in range(left + 1, right):
            self.dp[left][right] = min(
                self.dp[left][right],
                (self.__method1(left, i, cuts) +
                self.__method1(i, right, cuts) +
                (cuts[right] - cuts[left]))
            )
        return self.dp[left][right]

    def __method2 (self, cuts):
        for left in range(len(cuts) - 1, -1, -1):
            for right in range(left, len(cuts)):
                if ((right - left) <= 1):
                    self.dp[left][right] = 0
                    continue
                self.dp[left][right] = inf
                for i in range(left + 1, right):
                    self.dp[left][right] = min(
                        self.dp[left][right],
                        (self.dp[left][i] + self.dp[i][right] + (cuts[right] - cuts[left]))
                    )
        return self.dp[0][-1]

    def __method3 (self, cuts):
        knuth = [[0 for j in range(len(cuts))] for i in range(len(cuts))]
        for left in range(len(cuts) - 1, -1, -1):
            for right in range(left, len(cuts)):
                if ((right - left) <= 1):
                    self.dp[left][right] = 0
                    knuth[left][right] = left
                    continue
                self.dp[left][right] = inf
                for i in range(knuth[left][right - 1], knuth[left + 1][right] + 1):
                    curr_val = self.dp[left][i] + self.dp[i][right]
                    if (curr_val < self.dp[left][right]):
                        self.dp[left][right] = curr_val
                        knuth[left][right] = i
                self.dp[left][right] += (cuts[right] - cuts[left])
        return self.dp[0][-1]

    def minCost (self, n: int, cuts: List[int]) -> int:
        cuts.sort() ; cuts.insert(0, 0) ; cuts.append(n)
        self.dp = [[None for j in range(len(cuts))] for i in range(len(cuts))]
        #return self.__method1(0, len(cuts) - 1, cuts)
        #return self.__method2(cuts)
        return self.__method3(cuts)
