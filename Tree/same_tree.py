# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree (self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque() ; dq.append((p, q))
        while (dq):
            node1, node2 = dq.popleft()
            if ((node1) and (not node2)): return False
            if ((not node1) and (node2)): return False
            if ((not node1) and (not node2)): continue
            if (node1.val != node2.val): return False
            dq.append((node1.left, node2.left))
            dq.append((node1.right, node2.right))
        return True
