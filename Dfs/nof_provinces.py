from collections import deque

class UnionFind:
    def __init__ (self, n): self.parent = [[i, 1] for i in range(n)]
    def find (self, node):
        stk = deque()
        while (self.parent[node][0] != node):
            stk.append(node) ; node = self.parent[node][0]
        while (stk): self.parent[stk.pop()][0] = node
        return node
    def union (self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if (parent_a != parent_b):
            size_a, size_b = self.parent[parent_a][1], self.parent[parent_b][1]
            if (size_b > size_a):
                parent_a, parent_b = parent_b, parent_a
                size_a, size_b = size_b, size_a
            self.parent[parent_b][0] = parent_a
            self.parent[parent_a][1] += size_b
    def count_comps (self):
        count = 0
        for i in range(len(self.parent)):
            if (self.parent[i][0] == i): count += 1
        return count

class Solution:
    def __dfs (self, adj_lst):
        q, n, count = deque(), len(adj_lst), 0
        visited = [0 for i in range(n)]
        for i in range(n):
            if (visited[i] != 1):
                q.append(i) ; visited[i] = 1
                while (q):
                    curr_node = q.pop()
                    for next_node in range(n):
                        if ((adj_lst[curr_node][next_node] == 1) and (visited[next_node] != 1)):
                            q.append(next_node)
                            visited[next_node] = 1
                count += 1
        return count

    def __bfs (self, adj_lst):
        q, n, count = deque(), len(adj_lst), 0
        visited = [0 for i in range(n)]
        for i in range(n):
            if (visited[i] != 1):
                q.append(i) ; visited[i] = 1
                while (q):
                    curr_node = q.popleft()
                    for next_node in range(n):
                        if ((adj_lst[curr_node][next_node] == 1) and (visited[next_node] != 1)):
                            q.append(next_node)
                            visited[next_node] = 1
                count += 1
        return count

    def __uf (self, adj_lst):
        uf_obj = UnionFind(len(adj_lst))
        for i in range(len(adj_lst)):
            for j in range(len(adj_lst)):
                if (adj_lst[i][j] == 1): uf_obj.union(i, j)
        return uf_obj.count_comps()

    def findCircleNum (self, isConnected: List[List[int]]) -> int:
        #return self.__bfs(isConnected)
        #return self.__dfs(isConnected)
        return self.__uf(isConnected)
