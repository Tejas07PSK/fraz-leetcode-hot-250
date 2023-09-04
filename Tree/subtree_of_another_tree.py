# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __is_same (self, root, subRoot):
        if ((not root) or (not subRoot)): return ((not root) and (not subRoot))
        return ((root.val == subRoot.val) and self.__is_same(root.left, subRoot.left) and self.__is_same(root.right, subRoot.right))

    def __method1 (self, root, subRoot):
        if (root == None): return False
        if (self.__is_same(root, subRoot)): return True
        return (self.__method1(root.left, subRoot) or self.__method1(root.right, subRoot))

    def __serialize_tree (self, root, str_stk):
        if (not root):
            str_stk.append('#')
            return str_stk
        str_stk.append('^' + str(root.val))
        self.__serialize_tree(root.left, str_stk)
        self.__serialize_tree(root.right, str_stk)
        return str_stk

    def __method2 (self, root, subRoot):
        tree_sr = "".join(self.__serialize_tree(root, []))
        sub_tree_sr = "".join(self.__serialize_tree(subRoot, []))
        return sub_tree_sr in tree_sr

    def __recu_hash_tree (self, root, add_to_tree_hash_set):
        if (not root): return (3, 7)
        left1, left2 = self.__recu_hash_tree(root.left, add_to_tree_hash_set)
        right1, right2 = self.__recu_hash_tree(root.right, add_to_tree_hash_set)
        left1, left2 = (left1 << 5) % self.mod_1, (left2 << 7) % self.mod_2
        right1, right2 = (right1 << 1) % self.mod_1, (right2 << 1) % self.mod_2
        hp = ((left1 + right1 + root.val) % self.mod_1, (left2 + right2 + root.val) % self.mod_2)
        if (add_to_tree_hash_set): self.tree_hash_set.add(hp)
        return hp

    def __method3 (self, root, subRoot):
        self.mod_1, self.mod_2, self.tree_hash_set = 1000000007, 2147483647, set()
        self.__recu_hash_tree(root, True)
        sub_hp = self.__recu_hash_tree(subRoot, False)
        return sub_hp in self.tree_hash_set

    def isSubtree (self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #return self.__method1(root, subRoot)
        #return self.__method2(root, subRoot)
        return self.__method3(root, subRoot)
