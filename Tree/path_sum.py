# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def hasPathSum (self, root: Optional[TreeNode], targetSum: int) -> bool:
        if (not root): return False
        q = deque() ; q.append((root, root.val))
        while (q):
            curr_node, curr_sum = q.popleft()
            if ((not curr_node.left) and (not curr_node.right)):
                if (curr_sum == targetSum): return True
                continue
            if (curr_node.left): q.append((curr_node.left, curr_node.left.val + curr_sum))
            if (curr_node.right): q.append((curr_node.right, curr_node.right.val + curr_sum))
        return False
