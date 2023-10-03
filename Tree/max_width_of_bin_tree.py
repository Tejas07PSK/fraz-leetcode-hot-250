# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree (self, root: Optional[TreeNode]) -> int:
        q, ans = deque(), 0 ; q.append((1, root))
        while (q):
            curr_len = len(q)
            ans = max(ans, (q[-1][0] - q[0][0] + 1))
            while (curr_len > 0):
                curr_sl_no, curr_node = q.popleft()
                if (curr_node.left): q.append((2 * curr_sl_no + 1, curr_node.left))
                if (curr_node.right): q.append((2 * curr_sl_no + 2, curr_node.right))
                curr_len -= 1
        return ans
