# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def inorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        stk, ans = deque(), []
        while (root):
            stk.append(root)
            root = root.left
        while (stk):
            root = stk.pop()
            ans.append(root.val)
            root = root.right
            while (root):
                stk.append(root)
                root = root.left
        return ans
