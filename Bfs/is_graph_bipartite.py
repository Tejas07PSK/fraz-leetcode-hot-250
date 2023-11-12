from collections import deque

class Solution:
    def isBipartite (self, graph: List[List[int]]) -> bool:
        q, visited = deque(), [-1 for i in range(len(graph))]
        for node in range(len(graph)):
            if (visited[node] == -1):
                q.append(node)
                visited[node] = 0
                while (q):
                    curr_node = q.popleft()
                    curr_col = visited[curr_node]
                    for next_node in graph[curr_node]:
                        if (visited[next_node] == -1):
                            q.append(next_node)
                            visited[next_node] = curr_col ^ 1
                        elif (curr_col == visited[next_node]): return False
        return True
