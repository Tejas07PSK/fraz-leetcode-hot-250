class TrieNode:
    def __init__ (self, ch=''):
        self.ch = ch
        self.isEnd = False
        self.children = {}

class Solution:
    def __method1 (self, strs):
        root, ans = TrieNode(), []
        for string in strs:
            ptr = root
            for ch in string:
                if (ch not in ptr.children): ptr.children[ch] = TrieNode(ch)
                ptr = ptr.children[ch]
            ptr.isEnd = True
        while ((len(root.children) == 1) and (not root.isEnd)):
            for ch, node in root.children.items():
                root = node
                ans.append(ch)
        return "".join(ans)

    def __method2 (self, strs):
        if (len(strs) == 1): return strs[0]
        min_len, min_index = 201, 0
        for i in range(len(strs)):
            if (len(strs[i]) == 0): return ""
            if (len(strs[i]) < min_len): min_len, min_index = len(strs[i]), i
        strs[0], strs[min_index] = strs[min_index], strs[0]
        low, high = 0, len(strs[0]) - 1
        while (low <= high):
            mid = low + ((high - low) // 2)
            flag = True
            for i in range(1, len(strs)):
                j = 0
                while ((j <= mid) and (j < len(strs[i]))):
                    if (strs[i][j] != strs[0][j]):
                        flag = False
                        break
                    j += 1
                if (not flag): break
            if (flag): low = mid + 1
            else: high = mid - 1
        return strs[0][0:low]

    def longestCommonPrefix (self, strs: List[str]) -> str:
        #return self.__method1(strs)
        return self.__method2(strs)
