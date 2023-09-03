# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def __method1 (self, root):
        if (root == None): return root
        if (root.left != None): self.__method1(root.left)
        if (root.right != None): self.__method1(root.right)
        root.left, root.right = root.right, root.left
        return root

    def __method2 (self, root):
        if (not root): return root
        q = deque() ; q.append(root)
        while (q):
            cur_root = q.popleft()
            if (cur_root.left != None): q.append(cur_root.left)
            if (cur_root.right != None): q.append(cur_root.right)
            cur_root.left, cur_root.right = cur_root.right, cur_root.left
        return root

    def invertTree (self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #return self.__method1(root)
        return self.__method2(root)
