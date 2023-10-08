# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def __helper (self, root):
        left_pth = 0
        if (root.left): left_pth = max(left_pth, self.__helper(root.left))
        right_pth = 0
        if (root.right): right_pth = max(right_pth, self.__helper(root.right))
        self.res = max(self.res, left_pth + root.val + right_pth)
        return root.val + max(left_pth, right_pth)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -inf
        self.__helper(root)
        return self.res
