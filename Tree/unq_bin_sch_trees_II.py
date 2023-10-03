# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __helper (self, start, end):
        if (start > end): return [None]
        if ((start, end) in self.dp): return self.dp[(start, end)]
        curr_ans = []
        for idx in range(start, end + 1):
            possible_left_nodes = self.__helper(start, idx - 1)
            possible_right_nodes = self.__helper(idx + 1, end)
            for left_node in possible_left_nodes:
                for right_node in possible_right_nodes:
                    root = TreeNode(idx, left_node, right_node)
                    curr_ans.append(root)
        self.dp[(start, end)] = curr_ans
        return curr_ans

    def generateTrees (self, n: int) -> List[Optional[TreeNode]]:
        self.dp = {}
        return self.__helper(1, n)
