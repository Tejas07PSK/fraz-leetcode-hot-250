# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __helper (self, node):
        if (node in self.visited): return self.visited[node]
        ans = 0
        take = node.val
        max_from_left, max_from_right = 0, 0
        if (node.left):
            if (node.left.left): take += self.__helper(node.left.left)
            if (node.left.right): take += self.__helper(node.left.right)
        if (node.right):
            if (node.right.left): take += self.__helper(node.right.left)
            if (node.right.right): take += self.__helper(node.right.right)
        not_take = 0
        if (node.left): not_take += self.__helper(node.left)
        if (node.right): not_take += self.__helper(node.right)
        ans = max(take, not_take)
        self.visited[node] = ans
        return ans

    def rob (self, root: Optional[TreeNode]) -> int:
        self.visited = {}
        return self.__helper(root)
