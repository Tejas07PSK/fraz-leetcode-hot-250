# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __helper (self, root):
        if (not root): return True, 0
        if ((not root.left) and (not root.right)): return True, 1
        left_flag, left_ht = self.__helper(root.left) if (root.left) else (True, 0)
        if (not left_flag): return left_flag, left_ht
        right_flag, right_ht = self.__helper(root.right) if (root.right) else (True, 0)
        if (not right_flag): return right_flag, right_ht
        flag = True
        if (abs(left_ht - right_ht) > 1): flag = False
        return flag, 1 + max(left_ht, right_ht)

    def isBalanced (self, root: Optional[TreeNode]) -> bool:
        return self.__helper(root)[0]
