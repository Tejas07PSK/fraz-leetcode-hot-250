# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rangeSumBST (self, root: Optional[TreeNode], low: int, high: int) -> int:
        q, ans = deque(), 0
        q.append(root)
        while (q):
            curr_node = q.pop()
            if (low <= curr_node.val <= high):
                ans += curr_node.val
                if (curr_node.left != None): q.append(curr_node.left)
                if (curr_node.right != None): q.append(curr_node.right)
            if (curr_node.val < low):
                if (curr_node.right != None): q.append(curr_node.right)
            if (curr_node.val > high):
                if (curr_node.left != None): q.append(curr_node.left)
        return ans
