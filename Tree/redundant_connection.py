from collections import deque

class UnionFind:
    def __init__ (self, n):
        self.parents = [i for i in range(n + 1)]
        self.sizes = [1 for i in range(n + 1)]
        self.cap = n
    def find (self, node):
        stk = deque()
        while (self.parents[node] != node):
            stk.append(node)
            node = self.parents[node]
        while (stk):
            self.parents[stk.pop()] = node
        return node
    def union (self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if (parent1 != parent2):
            if (self.sizes[parent2] > self.sizes[parent1]):
                parent1, parent2 = parent2, parent1
            self.parents[parent2] = parent1
            self.sizes[parent1] += self.sizes[parent2]
            return True
        return False

class Solution:
    def findRedundantConnection (self, edges: List[List[int]]) -> List[int]:
        ans, uf = [None, None], UnionFind(len(edges))
        for start, end in edges:
            if (not uf.union(start, end)): ans[0], ans[1] = start, end
        return ans
