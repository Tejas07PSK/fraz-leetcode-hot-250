from collections import deque

class UnionFind:
    def __init__ (self, n):
        self.parents = [i for i in range(n + 1)]
        self.sizes = [1 for i in range(n + 1)]
        self.n = n

    def find (self, node):
        stk = deque()
        while (node != self.parents[node]):
            stk.append(node)
            node = self.parents[node]
        while (stk): self.parents[stk.pop()] = node
        return node

    def union (self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if (parent1 != parent2):
            if (self.sizes[parent1] < self.sizes[parent2]): parent1, parent2 = parent2, parent1
            self.parents[parent2] = parent1
            self.sizes[parent1] += self.sizes[parent2]

class Solution:
    def numIslands (self, grid: List[List[str]]) -> int:
        uf = UnionFind(len(grid) * len(grid[0]))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr_cell = row * len(grid[0]) + col + 1
                if (grid[row][col] == "0"):
                    uf.parents[curr_cell] = -1
                    continue
                for row_offset, col_offset in directions:
                    next_row = row + row_offset
                    next_col = col + col_offset
                    next_cell = next_row * len(grid[0]) + next_col + 1
                    if ((0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0])) and (grid[next_row][next_col] == "1")):
                        uf.union(curr_cell, next_cell)
        ans = 0
        for i in range(1, len(uf.parents)):
            if (i == uf.parents[i]): ans += 1
        return ans
