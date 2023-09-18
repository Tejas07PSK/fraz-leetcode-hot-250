# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes (self, root: TreeNode) -> int:
        q, ans = deque(), 0
        q.append((root, root.val))
        while (q):
            curr_node, max_so_far = q.pop()
            if (curr_node.val >= max_so_far): ans += 1
            if (curr_node.left): q.append((curr_node.left, max(max_so_far, curr_node.left.val)))
            if (curr_node.right): q.append((curr_node.right, max(max_so_far, curr_node.right.val)))
        return ans
