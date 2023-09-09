# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth (self, root: Optional[TreeNode]) -> int:
        if (not root): return 0
        q, level = deque(), 0
        q.append(root)
        while (q):
            curr_sz = len(q)
            level += 1
            while (curr_sz > 0):
                curr_node = q.popleft()
                if (curr_node.left): q.append(curr_node.left)
                if (curr_node.right): q.append(curr_node.right)
                curr_sz -= 1
        return level
