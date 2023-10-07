# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    def serialize (self, root):
        if (not root): return 'N'
        q, ans = deque([root]), [str(root.val)]
        while (q):
            curr_sz = len(q)
            while (curr_sz > 0):
                curr_node = q.popleft()
                if (curr_node.left):
                    q.append(curr_node.left)
                    ans.append(str(curr_node.left.val))
                else: ans.append('N')
                if (curr_node.right):
                    q.append(curr_node.right)
                    ans.append(str(curr_node.right.val))
                else: ans.append('N')
                curr_sz -= 1
        while (ans[-1] == 'N'): ans.pop()
        return ",".join(ans)

    def deserialize (self, data):
        arr = data.split(',')
        for i in range(len(arr)):
            if (arr[i] != 'N'): arr[i] = TreeNode(int(arr[i]))
            else: arr[i] = None
        j = 0
        for i in range(len(arr)):
            if (arr[i] == None): continue
            lft_idx, rt_idx = j + 1, j + 2
            if (lft_idx < len(arr)): arr[i].left = arr[lft_idx]
            if (rt_idx < len(arr)): arr[i].right = arr[rt_idx]
            j += 2
        return arr[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
