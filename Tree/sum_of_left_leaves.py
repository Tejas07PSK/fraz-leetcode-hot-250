# Definition for a binary tree node.
# class TreeNode:
#     def __init__ (self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __helper (self, root):
        if (not root): return root
        if ((not root.left) and (not root.right)): return root
        if (root.left):
            from_left = self.__helper(root.left)
            if (from_left): self.ans += from_left.val
        if (root.right): self.__helper(root.right)
        return None

    def sumOfLeftLeaves (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.__helper(root)
        return self.ans
