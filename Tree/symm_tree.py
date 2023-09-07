# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric (self, root: Optional[TreeNode]) -> bool:
        q1, q2 = deque(), deque()
        if (root.left): q1.append((root.left, 1, root, 1))
        if (root.right): q2.append((root.right, 1, root, 1))
        while ((q1) or (q2)):
            if (len(q1) != len(q2)): return False
            curr_len = len(q1)
            while (curr_len > 0):
                curr_node1, curr_node1_dir, curr_node1_par, curr_node1_par_dir = q1.popleft()
                curr_node2, curr_node2_dir, curr_node2_par, curr_node2_par_dir = q2.popleft()
                if (
                    (curr_node1.val != curr_node2.val) or
                    (curr_node1_dir != curr_node2_dir) or
                    (curr_node1_par.val != curr_node2_par.val) or
                    (curr_node1_par_dir != curr_node2_par_dir)
                ): return False
                if (curr_node1.left): q1.append((curr_node1.left, 1, curr_node1, curr_node1_dir))
                if (curr_node1.right): q1.append((curr_node1.right, -1, curr_node1, curr_node1_dir))
                if (curr_node2.right): q2.append((curr_node2.right, 1, curr_node2, curr_node2_dir))
                if (curr_node2.left): q2.append((curr_node2.left, -1, curr_node2, curr_node2_dir))
                curr_len -= 1
        return True
