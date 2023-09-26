# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __dfs_helper (self, curr_sum, root, tgs, hm):
        res = 0
        curr_sum += root.val
        if ((curr_sum - tgs) in hm): res += hm[curr_sum - tgs]
        if (curr_sum not in hm): hm[curr_sum] = 1
        else: hm[curr_sum] += 1
        if (root.left): res += self.__dfs_helper(curr_sum, root.left, tgs, hm)
        if (root.right): res += self.__dfs_helper(curr_sum, root.right, tgs, hm)
        hm[curr_sum] -= 1
        if (hm[curr_sum] == 0): del hm[curr_sum]
        curr_sum -= root.val
        return res

    def pathSum (self, root: Optional[TreeNode], targetSum: int) -> int:
        if (not root): return 0
        return self.__dfs_helper(0, root, targetSum, {0:1})
