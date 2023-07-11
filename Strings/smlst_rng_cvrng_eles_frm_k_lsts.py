from heapq import heappop, heappush
from math import inf

class Solution:
    def smallestRange (self, nums: List[List[int]]) -> List[int]:
        hp, curr_right = [], -inf
        ans = [-inf, inf]
        for i in range(len(nums)):
            heappush(hp, (nums[i][0], i, 0))
            curr_right = max(curr_right, nums[i][0])
        while (hp):
            curr_left, i, j = heappop(hp)
            if ((curr_right - curr_left) < (ans[1] - ans[0])):
                ans[0], ans[1] = curr_left, curr_right
            if ((j + 1) == len(nums[i])): return ans
            curr_right = max(curr_right, nums[i][j + 1])
            heappush(hp, (nums[i][j + 1], i, j + 1))
        return ans
