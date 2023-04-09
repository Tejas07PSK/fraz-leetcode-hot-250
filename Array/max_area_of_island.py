from collections import deque

class UnionFind:
    def __init__ (self): self.graph = {}
    def find (self, node):
        if (node not in self.graph):
            self.graph[node] = [node, 1]
            return node
        stk = deque()
        while (self.graph[node][0] != node):
            stk.append(node)
            node = self.graph[node][0]
        while (stk): self.graph[stk.pop()][0] = node
        return node
    def union (self, node1, node2):
        node1, node2 = self.find(node1), self.find(node2)
        if (node1 != node2):
            if (self.graph[node1][1] < self.graph[node2][1]): node1, node2 = node2, node1
            self.graph[node2][0] = node1
            self.graph[node1][1] += self.graph[node2][1]
    def get_largest_comp_size (self):
        print(self.graph)
        ans = 0
        for node in self.graph.keys():
            if (self.graph[node][0] == node): ans = max(ans, self.graph[node][1])
        return ans

class Solution:
    def __dfs_helper (self, i, j, grid):
        self.curr_sz += 1
        grid[i][j] = -grid[i][j]
        for row_offset, col_offset in self.dirs:
            next_i, next_j = i + row_offset, j + col_offset
            if ((0 <= next_i < len(grid)) and (0 <= next_j < len(grid[0])) and (grid[next_i][next_j] == 1)):
                self.__dfs_helper(next_i, next_j, grid)

    def __method1 (self, grid):
        ans, self.curr_sz = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    self.__dfs_helper(i, j, grid)
                    ans = max(ans, self.curr_sz)
                    self.curr_sz = 0
        return ans

    def __method2 (self, grid):
        uf = UnionFind()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    node1 = (i, j)
                    for row_offset, col_offset in self.dirs:
                        next_i, next_j = i + row_offset, j + col_offset
                        if ((0 <= next_i < len(grid)) and (0 <= next_j < len(grid[0])) and (grid[next_i][next_j] == 1)):
                            node2 = (next_i, next_j)
                            uf.union(node1, node2)
        return uf.get_largest_comp_size()

    def maxAreaOfIsland (self, grid: List[List[int]]) -> int:
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return self.__method1(grid)
