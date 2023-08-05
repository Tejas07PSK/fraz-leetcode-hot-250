class Solution:
    def minCost (self, colors: str, neededTime: List[int]) -> int:
        i, j, ans = 0, 1, 0
        while (j < len(colors)):
            if (colors[i] != colors[j]): i = j
            else:
                if (neededTime[i] <= neededTime[j]):
                    ans += neededTime[i]
                    i = j
                else: ans += neededTime[j]
            j += 1
        return ans
