# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def __dfs_helper (self, root):
        if (not root): return 0, 0, True
        curr_max, curr_min = root.val, root.val
        curr_left_state, curr_right_state = True, True
        if (root.left):
            max_from_left, min_from_left, left_state = self.__dfs_helper(root.left)
            if (not left_state): return max_from_left, min_from_left, left_state
            curr_left_state = (root.val > root.left.val) and (root.val > max_from_left)
            curr_max = max(curr_max, max_from_left)
            curr_min = min(curr_min, min_from_left)
        if (root.right):
            max_from_right, min_from_right, right_state = self.__dfs_helper(root.right)
            if (not right_state): return max_from_right, min_from_right, right_state
            curr_right_state = (root.val < root.right.val) and (root.val < min_from_right)
            curr_max = max(curr_max, max_from_right)
            curr_min = min(curr_min, min_from_right)
        return curr_max, curr_min, (curr_left_state and curr_right_state)

    def __in_order_trav_helper (self, root):
        prev, stk = None, deque()
        while (root):
            stk.append(root)
            root = root.left
        while (stk):
            root = stk.pop()
            if ((prev) and (root.val <= prev.val)): return False
            prev = root
            if (root.right):
                root = root.right
                while (root):
                    stk.append(root)
                    root = root.left
        return True

    def isValidBST (self, root: Optional[TreeNode]) -> bool:
        #return self.__dfs_helper(root)[2]
        return self.__in_order_trav_helper(root)
