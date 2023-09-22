# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def __formGraph (self, root):
        q, graph = deque(), {root.val: []} ; q.append(root)
        while (q):
            curr_node = q.popleft()
            if (curr_node.left):
                graph[curr_node.left.val] = [curr_node.val]
                graph[curr_node.val].append(curr_node.left.val)
                q.append(curr_node.left)
            if (curr_node.right):
                graph[curr_node.right.val] = [curr_node.val]
                graph[curr_node.val].append(curr_node.right.val)
                q.append(curr_node.right)
        return graph

    def distanceK (self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = self.__formGraph(root)
        q, visited = deque(), set() ; q.append((target.val, 0)) ; visited.add(target.val)
        ans = []
        while (q):
            curr_node, curr_dist = q.popleft()
            if (curr_dist == k):
                ans.append(curr_node)
                continue
            for next_node in graph[curr_node]:
                if (next_node not in visited):
                    q.append((next_node, curr_dist + 1))
                    visited.add(next_node)
        return ans
