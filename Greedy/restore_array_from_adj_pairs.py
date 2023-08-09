from collections import deque

class Solution:
    def restoreArray (self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for start, end in adjacentPairs:
            if (start not in graph): graph[start] = []
            graph[start].append(end)
            if (end not in graph): graph[end] = []
            graph[end].append(start)
        root = None
        for node in graph:
            if (len(graph[node]) == 1):
                root = node
                break
        res, q, parent = [], deque(), None
        q.append(root)
        while (q):
            curr_node = q.pop()
            res.append(curr_node)
            count = 0
            for next_node in graph[curr_node]:
                if (next_node != parent):
                    q.append(next_node)
                    count += 1
                    break
            if (count == 0): return res
            parent = curr_node
        return res
