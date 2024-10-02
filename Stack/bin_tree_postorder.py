# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def postorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while (root):
            if (not root.right):
                ans.append(root.val)
                root = root.left
            else:
                temp = root.right
                while ((temp.left) and (temp.left != root)): temp = temp.left
                if (not temp.left):
                    temp.left = root
                    ans.append(root.val)
                    root = root.right
                else:
                    temp.left = None
                    root = root.left
        return reversed(ans)
