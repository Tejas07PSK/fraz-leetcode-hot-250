from collections import deque

class Solution:
    def allPathsSourceTarget (self, graph: List[List[int]]) -> List[List[int]]:
        q, ans = deque(), [] ; q.append((0, [0]))
        while (q):
            curr_node, curr_path = q.popleft()
            for next_node in graph[curr_node]:
                next_path = curr_path + [next_node]
                if (next_node == (len(graph) - 1)): ans.append(next_path)
                else: q.append((next_node, next_path))
        return ans
