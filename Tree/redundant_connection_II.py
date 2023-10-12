from collections import deque

class UnionFind:
    def __init__ (self, n):
        self.parents = [i for i in range(n + 1)]
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
            self.parents[parent2] = parent1
            return True
        return False

class Solution:
    def findRedundantDirectedConnection (self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        bad_edge1_idx, bad_edge2_idx = None, None
        in_deg = [None for i in range(len(edges) + 1)]
        for i in range(len(edges)):
            start, end = edges[i]
            if (in_deg[end] == None): in_deg[end] = i
            else:
                 bad_edge1_idx = in_deg[end]
                 bad_edge2_idx = i
        for i in range(len(edges)):
            if ((bad_edge2_idx != None) and (i == bad_edge2_idx)): continue
            start, end = edges[i]
            if (not uf.union(start, end)): return edges[i] if (bad_edge1_idx == None) else edges[bad_edge1_idx]
        return edges[bad_edge2_idx]
