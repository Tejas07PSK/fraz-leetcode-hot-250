# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev_node, first, second, stk = None, None, None, deque()
        while (root):
            if (not root.left):
                if (prev_node and (root.val < prev_node.val)):
                    if (not first): first = prev_node
                    if (first): second = root
                prev_node = root
                root = root.right
            else:
                temp = root.left
                while ((temp.right) and (temp.right != root)): temp = temp.right
                if (not temp.right):
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None
                    if (prev_node and (root.val < prev_node.val)):
                        if (not first): first = prev_node
                        if (first): second = root
                    prev_node = root
                    root = root.right
        first.val, second.val = second.val, first.val
