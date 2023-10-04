# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest (self, root: Optional[TreeNode], k: int) -> int:
        while (root):
            if (not root.left):
                k -= 1
                if (k == 0): return root.val
                root = root.right
            else:
                temp = root.left
                while ((temp.right) and (temp.right != root)): temp = temp.right
                if (not temp.right):
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None
                    k -= 1
                    if (k == 0): return root.val
                    root = root.right
        return -1
