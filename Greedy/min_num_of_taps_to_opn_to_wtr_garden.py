class Solution:
    def minTaps (self, n: int, ranges: List[int]) -> int:
        jumps = [0 for i in range(0, n + 1)]
        for i in range(0, n + 1):
            curr_start, curr_end = max(0, i - ranges[i]), min(n, i + ranges[i])
            jumps[curr_start] = max(jumps[curr_start], curr_end)
        taps, curr_end, next_end = 0, 0, 0
        for i in range(n + 1):
            if (i > next_end): return -1
            if (i > curr_end):
                taps += 1
                curr_end = next_end
            next_end = max(next_end, jumps[i])
        return taps
