# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class BSTIterator:

    def __init__ (self, root: Optional[TreeNode]):
        self.stk = deque()
        while (root):
            self.stk.append(root)
            root = root.left

    def next (self) -> int:
        if (self.hasNext()):
            curr_node = self.stk.pop()
            ans = curr_node.val
            if (curr_node.right):
                curr_node = curr_node.right
                while (curr_node):
                    self.stk.append(curr_node)
                    curr_node = curr_node.left
            return ans
        return -1

    def hasNext (self) -> bool: return bool(self.stk)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
