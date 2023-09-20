# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor (self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if ((root == p) or (root == q)): return root
        from_left, from_right = None, None
        if (root.left): from_left = self.lowestCommonAncestor(root.left, p, q)
        if (root.right): from_right = self.lowestCommonAncestor(root.right, p, q)
        if ((from_left) and (from_right)): return root
        if ((from_left) and (not from_right)): return from_left
        if ((not from_left) and (from_right)): return from_right
        return None
