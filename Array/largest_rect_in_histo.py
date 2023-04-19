from collections import deque
class Solution:
    def largestRectangleArea (self, heights: List[int]) -> int:
        ans, dq = 0, deque()
        for i in range(len(heights)):
            current_bar = [heights[i], 1]
            prev_pop_bar = [0, 0]
            while ((dq) and (dq[-1][0] >= current_bar[0])):
                temp_bar = dq.pop()
                prev_pop_bar[0] = temp_bar[0]
                prev_pop_bar[1] += temp_bar[1]
                ans = max(ans, (prev_pop_bar[0] * prev_pop_bar[1])) 
                current_bar[1] += temp_bar[1]
            ans = max(ans, (current_bar[0] * current_bar[1]))
            dq.append(current_bar)
        current_bar = dq.pop()
        while (dq):
            current_bar[0] = dq[-1][0]
            current_bar[1] += dq[-1][1]
            ans = max(ans, (current_bar[0] * current_bar[1]))
            dq.pop()
        return ans
