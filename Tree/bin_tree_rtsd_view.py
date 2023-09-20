# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView (self, root: Optional[TreeNode]) -> List[int]:
        if (not root): return []
        dq = deque() ; dq.append(root)
        res = []
        while (dq):
            curr_sz = len(dq)
            flag = False
            while (curr_sz > 0):
                curr_node = dq.pop()
                if (not flag):
                    res.append(curr_node.val)
                    flag = True
                if (curr_node.right): dq.appendleft(curr_node.right)
                if (curr_node.left): dq.appendleft(curr_node.left)
                curr_sz -= 1
        return res
