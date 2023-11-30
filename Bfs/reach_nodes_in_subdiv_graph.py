from heapq import heappop, heappush
from math import inf

class Solution:
    def reachableNodes (self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph, dists = [[] for i in range(n)], [inf for i in range(n)]
        for start, end, wt in edges:
            graph[start].append((end, wt))
            graph[end].append((start, wt))
        ans, hp, used = 0, [(0, 0)], {}
        dists[0] = 0
        while (hp):
            curr_dist, curr_node = heappop(hp)
            if (curr_dist > dists[curr_node]): continue
            ans += 1
            for next_node, next_wt in graph[curr_node]:
                used[(curr_node, next_node)] = min(next_wt, maxMoves - curr_dist)
                next_dist = curr_dist + next_wt + 1
                if (next_dist > maxMoves): continue
                if (dists[next_node] > next_dist):
                    heappush(hp, (next_dist, next_node))
                    dists[next_node] = next_dist
        for start, end, wt in edges: ans += min(wt, used.get((start, end), 0) + used.get((end, start), 0))
        return ans
