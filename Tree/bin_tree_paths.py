# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __dfs_helper (self, root, curr_path):
        root_str_val = str(root.val)
        curr_path.append(root_str_val)
        if ((not root.left) and (not root.right)):
            self.ans.append("->".join(curr_path))
            curr_path.pop()
            return
        if (root.left): self.__dfs_helper(root.left, curr_path)
        if (root.right): self.__dfs_helper(root.right, curr_path)
        curr_path.pop()

    def binaryTreePaths (self, root: Optional[TreeNode]) -> List[str]:
        if (not root): return []
        self.ans = []
        self.__dfs_helper(root, [])
        return self.ans
