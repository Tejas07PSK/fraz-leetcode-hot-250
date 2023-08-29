from collections import deque

class UnionFind:
    def __init__ (self, n): self.parents = [[i, 1] for i in range(n)]
    def find (self, node):
        stk = deque()
        while (self.parents[node][0] != node):
            stk.append(node)
            node = self.parents[node][0]
        while (stk): self.parents[stk.pop()][0] = node
        return node
    def union (self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if (parent1 == parent2): return parent1, self.parents[parent1][1]
        size1, size2 = self.parents[parent1][1], self.parents[parent2][1]
        if (size2 > size1):
            parent1, parent2 = parent2, parent1
            size1, size2 = size2, size1
        self.parents[parent2][0] = parent1
        self.parents[parent1][1] += size2
        return parent1, self.parents[parent1][1]

class Solution:
    def largestIsland (self, grid: List[List[int]]) -> int:
        dirs, sz = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)], len(grid[0])
        ans, uf = 0, UnionFind(sz * sz)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    curr_node = sz * i + j
                    for i_offset, j_offset in dirs:
                        next_i, next_j = i + i_offset, j + j_offset
                        if ((0 <= next_i < sz) and (0 <= next_j < sz) and (grid[next_i][next_j] == 1)):
                            next_node = sz * next_i + next_j
                            final_parent, final_size = uf.union(curr_node, next_node)
                            ans = max(ans, final_size)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 0):
                    curr_node, neib_isls = sz * i + j, set()
                    for i_offset, j_offset in dirs:
                        next_i, next_j = i + i_offset, j + j_offset
                        if ((0 <= next_i < sz) and (0 <= next_j < sz) and (grid[next_i][next_j] == 1)):
                            next_node = sz * next_i + next_j
                            neib_isls.add(uf.find(next_node))
                    temp_ans = 0
                    for neib_node in neib_isls: temp_ans += uf.parents[neib_node][1]
                    ans = max(ans, temp_ans + 1)
        return ans
