from heapq import heappop, heappush
class Solution:
    def maxEvents (self, events: List[List[int]]) -> int:
        events.sort()
        i, d, ans, hp = 0, 0, 0, []
        while ((i < len(events)) or hp):
            if (not hp):
                d = events[i][0]
            while ((i < len(events)) and (events[i][0] <= d)):
                heappush(hp, events[i][1])
                i += 1
            heappop(hp)
            d += 1 ; ans += 1
            while (hp) and (hp[0] < d): heappop(hp)
        return ans
