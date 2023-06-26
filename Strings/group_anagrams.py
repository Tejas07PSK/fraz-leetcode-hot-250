class TrieNode:
    def __init__ (self):
        self.children = {}
        self.group_idx = None

class Solution:
    def groupAnagrams (self, strs: List[str]) -> List[List[str]]:
        res, groups = [], 0
        tri_root = TrieNode()
        for string in strs:
            ptr = tri_root
            for ch in sorted(string):
                if (ch not in ptr.children): ptr.children[ch] = TrieNode()
                ptr = ptr.children[ch]
            if (ptr.group_idx == None):
                res.append([]) ; ptr.group_idx = groups ; groups += 1
            res[ptr.group_idx].append(string)
        return res
