# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder (self, root: Optional[TreeNode]) -> List[List[int]]:
        if (not root): return []
        q, ans = deque(), []
        q.append(root)
        while (q):
            curr_lvl, curr_lvl_sz = [], len(q)
            while (curr_lvl_sz > 0):
                curr_node = q.popleft()
                curr_lvl.append(curr_node.val)
                if (curr_node.left): q.append(curr_node.left)
                if (curr_node.right): q.append(curr_node.right)
                curr_lvl_sz -= 1
            ans.append(curr_lvl)
        return ans
