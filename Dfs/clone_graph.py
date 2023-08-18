"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def __dfs_helper (self, node):
        if (node == None): return None
        clone_node = Node(node.val, []) ; self.visited[node] = clone_node
        if (node.neighbors != None):
            for next_node in node.neighbors:
                if (next_node not in self.visited):
                    next_node_clone = self.__dfs_helper(next_node)
                    clone_node.neighbors.append(next_node_clone)
                else: clone_node.neighbors.append(self.visited[next_node])
        return clone_node

    def __bfs_helper (self, node):
        if (node == None): return None
        q = deque() ; self.visited[node] = Node(node.val, [])
        q.append((node, self.visited[node]))
        while (q):
            curr_node, curr_node_clone = q.popleft()
            if (curr_node.neighbors != None):
                for next_node in curr_node.neighbors:
                    if (next_node not in self.visited):
                        next_clone = Node(next_node.val, [])
                        curr_node_clone.neighbors.append(next_clone)
                        self.visited[next_node] = next_clone
                        q.append((next_node, next_clone))
                    else: curr_node_clone.neighbors.append(self.visited[next_node])
        return self.visited[node]

    def cloneGraph (self, node: 'Node') -> 'Node':
        self.visited = {}
        #return self.__dfs_helper(node)
        return self.__bfs_helper(node)
