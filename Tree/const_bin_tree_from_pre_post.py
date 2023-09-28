# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def constructFromPrePost (self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stk, root, j = deque(), TreeNode(preorder[0]), 0
        stk.append(root)
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            while (stk[-1].val == postorder[j]):
                stk.pop()
                j += 1
            if (not stk[-1].left): stk[-1].left = node
            else: stk[-1].right = node
            stk.append(node)
        return root
