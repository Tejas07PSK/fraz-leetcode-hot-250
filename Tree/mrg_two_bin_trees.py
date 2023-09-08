# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def mergeTrees (self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if ((not root1) and (not root2)): return None
        q, root = deque(), TreeNode()
        q.append((root1, root2, root))
        while (q):
            node1, node2, copy_node = q.popleft()
            copy_node.val = (node1.val if (node1) else 0) + (node2.val if (node2) else 0)
            next_left1, next_left2 =  (node1.left if (node1) else None), (node2.left if (node2) else None)
            next_right1, next_right2 =  (node1.right if (node1) else None), (node2.right if (node2) else None)
            if (next_left1 or next_left2):
                next_left_copy_node = TreeNode() ; copy_node.left = next_left_copy_node
                q.append((next_left1, next_left2, next_left_copy_node))
            if (next_right1 or next_right2):
                next_right_copy_node = TreeNode() ; copy_node.right = next_right_copy_node
                q.append((next_right1, next_right2, next_right_copy_node))
        return root
