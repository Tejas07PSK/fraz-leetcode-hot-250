# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __helper (self, left, right, nums):
        if (left > right): return None
        if (left == right): return TreeNode(nums[left])
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid], self.__helper(left, mid - 1, nums), self.__helper(mid + 1, right, nums))
        return root

    def sortedArrayToBST (self, nums: List[int]) -> Optional[TreeNode]:
        return self.__helper(0, len(nums) - 1, nums)
