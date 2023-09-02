# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def __helper (self, root):
        max_from_left, max_from_right = 0, 0
        if (root.left != None): max_from_left = 1 + self.__helper(root.left)
        if (root.right != None): max_from_right = 1 + self.__helper(root.right)
        self.ans = max(self.ans, (max_from_left + max_from_right))
        return max(max_from_left, max_from_right)

    def diameterOfBinaryTree (self, root: Optional[TreeNode]) -> int:
        self.ans = 0 ; self.__helper(root)
        return self.ans
