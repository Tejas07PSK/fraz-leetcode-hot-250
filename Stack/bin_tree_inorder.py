# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def inorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while (root):
            if (not root.left):
                ans.append(root.val)
                root = root.right
            else:
                temp = root.left
                while ((temp.right) and (temp.right != root)): temp = temp.right
                if (not temp.right):
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None
                    ans.append(root.val)
                    root = root.right
        return ans
