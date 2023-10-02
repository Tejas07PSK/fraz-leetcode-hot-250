# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten (self, root: Optional[TreeNode]) -> None:
        ptr = root
        while (ptr):
            if (not ptr.left): ptr = ptr.right
            else:
                temp = ptr.left
                while ((temp.right) and (temp.right != ptr)): temp = temp.right
                if (not temp.right):
                    temp.right = ptr
                    ptr = ptr.left
                else:
                    tmp = ptr.right
                    ptr.right = ptr.left
                    ptr.left = None
                    temp.right = tmp
                    ptr = tmp
        return root
