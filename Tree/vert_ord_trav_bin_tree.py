# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __dfs_helper (self, root, v_lvl, lvl):
        if (v_lvl not in self.hm): self.hm[v_lvl] = {}
        if (lvl not in self.hm[v_lvl]): self.hm[v_lvl][lvl] = []
        self.hm[v_lvl][lvl].append(root.val)
        if (root.left): self.__dfs_helper(root.left, v_lvl - 1, lvl + 1)
        if (root.right): self.__dfs_helper(root.right, v_lvl + 1, lvl + 1)

    def __bfs_helper (self, root):
        q = deque() ; q.append((root, 0, 0))
        while (q):
            node, v_lvl, lvl = q.popleft()
            if (v_lvl not in self.hm): self.hm[v_lvl] = {}
            if (lvl not in self.hm[v_lvl]): self.hm[v_lvl][lvl] = []
            self.hm[v_lvl][lvl].append(node.val)
            if (node.left): q.append((node.left, v_lvl - 1, lvl + 1))
            if (node.right): q.append((node.right, v_lvl + 1, lvl + 1))

    def verticalTraversal (self, root: Optional[TreeNode]) -> List[List[int]]:
        self.hm, res = {}, []
        #self.__dfs_helper(root, 0, 0)
        self.__bfs_helper(root)
        for col in sorted(self.hm.keys()):
            temp = []
            for row in sorted(self.hm[col].keys()): temp.extend(sorted(self.hm[col][row]))
            res.append(temp)
        return res
