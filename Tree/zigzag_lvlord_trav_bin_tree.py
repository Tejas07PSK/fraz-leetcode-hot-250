# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder (self, root: Optional[TreeNode]) -> List[List[int]]:
        if (not root): return []
        dq, lvl, ans = deque(), 0, []
        dq.append(root)
        while (dq):
            curr_lvl_ans = []
            curr_lvl_sz = len(dq)
            while (curr_lvl_sz > 0):
                if ((lvl & 1) == 0):
                    curr_node = dq.popleft()
                    curr_lvl_ans.append(curr_node.val)
                    if (curr_node.left): dq.append(curr_node.left)
                    if (curr_node.right): dq.append(curr_node.right)
                else:
                    curr_node = dq.pop()
                    curr_lvl_ans.append(curr_node.val)
                    if (curr_node.right): dq.appendleft(curr_node.right)
                    if (curr_node.left): dq.appendleft(curr_node.left)
                curr_lvl_sz -= 1
            ans.append(curr_lvl_ans)
            lvl += 1
        return ans
