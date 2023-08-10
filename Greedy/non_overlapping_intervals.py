class Solution:
    def eraseOverlapIntervals (self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i, j, ans = 0, 1, 0
        while (j < len(intervals)):
            if (intervals[j][0] < intervals[i][1]):
                ans += 1
                if (intervals[i][1] >= intervals[j][1]): i = j
            else: i = j
            j += 1
        return ans
