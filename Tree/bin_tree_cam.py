# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from enum import Enum

class Cam(Enum):
    COVERED = 1
    HAS_CAM = 2
    NOT_COVERED = 3

class Solution:
    def __dfs_helper (self, root):
        l, r = Cam.COVERED, Cam.COVERED
        if (root.left): l = self.__dfs_helper(root.left)
        if (root.right): r = self.__dfs_helper(root.right)
        if ((l == Cam.NOT_COVERED) or (r == Cam.NOT_COVERED)):
            self.ans += 1
            return Cam.HAS_CAM
        if ((l == Cam.HAS_CAM) or (r == Cam.HAS_CAM)): return Cam.COVERED
        return Cam.NOT_COVERED

    def minCameraCover (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if (self.__dfs_helper(root) == Cam.NOT_COVERED): self.ans += 1
        return self.ans
