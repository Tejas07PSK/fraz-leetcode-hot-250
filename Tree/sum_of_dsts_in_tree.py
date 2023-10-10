class Solution:
    def __dfs1 (self, root, parent):
        for next_node in self.graph[root]:
            if (next_node != parent):
                self.__dfs1(next_node, root)
                self.count[root] += self.count[next_node]
                self.res[root] += self.res[next_node] + self.count[next_node]

    def __dfs2 (self, root, parent):
        for next_node in self.graph[root]:
            if (next_node != parent):
                self.res[next_node] = self.res[root] - self.count[next_node] + self.n - self.count[next_node]
                self.__dfs2(next_node, root)

    def sumOfDistancesInTree (self, n: int, edges: List[List[int]]) -> List[int]:
        self.res, self.count = [0 for i in range(n)], [1 for i in range(n)]
        self.graph, self.n = [[] for i in range(n)], n
        for start, end in edges:
            self.graph[start].append(end)
            self.graph[end].append(start)
        self.__dfs1(0, -1)
        self.__dfs2(0, -1)
        return self.res
