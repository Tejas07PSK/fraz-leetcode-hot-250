class Solution:
    def __dfs_helper (self, parent, curr_node):
        self.in_time += 1
        curr_time, curr_min_time = self.in_time, self.in_time
        self.visited[curr_node] = curr_time
        for next_node in self.graph[curr_node]:
            if (next_node != parent):
                next_time = curr_time
                if (self.visited[next_node] != -1): next_time = self.visited[next_node]
                else: next_time = self.__dfs_helper(curr_node, next_node)
                if (next_time > curr_time): self.ans.append([curr_node, next_node])
                curr_min_time = min(curr_min_time, next_time)
        self.visited[curr_node] = curr_min_time
        return curr_min_time

    def criticalConnections (self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.visited, self.in_time, self.graph, self.ans = [-1 for i in range(n)], 0, [[] for i in range(n)], []
        for start, end in connections:
            self.graph[start].append(end)
            self.graph[end].append(start)
        self.__dfs_helper(-1, 0)
        return self.ans
