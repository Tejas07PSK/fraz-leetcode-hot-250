# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __in_order_helper (self, root):
        if (not root): return
        if (root.left): self.__in_order_helper(root.left)
        if (self.prev):
            self.ans = min(self.ans, root.val - self.prev.val)
        self.prev = root
        if (root.right): self.__in_order_helper(root.right)

    def getMinimumDifference (self, root: Optional[TreeNode]) -> int:
        self.ans, self.prev = 100001, None
        self.__in_order_helper(root)
        return self.ans
