class TrieNode:
    def __init__ (self):
        self.is_word_end = False
        self.char = '*'
        self.children = {}

class Solution:
    def __method1 (self, i, s):
        if (i == len(s)): return True
        if (self.dp[i] != None): return self.dp[i]
        self.dp[i] = False
        ptr = self.trie_root
        for j in range(i, len(s)):
            if (s[j] not in ptr.children): break
            ptr = ptr.children[s[j]]
            if ((ptr.is_word_end) and (self.__method1(j + 1, s))):
                self.dp[i] = True ; break
        return self.dp[i]

    def __method2 (self, s):
        self.dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            self.dp[i] = False
            ptr = self.trie_root
            for j in range(i, len(s)):
                if (s[j] not in ptr.children): break
                ptr = ptr.children[s[j]]
                if ((ptr.is_word_end) and (self.dp[j + 1])):
                    self.dp[i] = True ; break
        return self.dp[0]

    def wordBreak (self, s: str, wordDict: List[str]) -> bool:
        self.dp = [None for i in range(len(s) + 1)]
        self.trie_root = TrieNode()
        for word in wordDict:
            ptr = self.trie_root
            for ch in word:
                if (ch not in ptr.children):
                    ptr.children[ch] = TrieNode()
                    ptr.children[ch].char = ch
                ptr = ptr.children[ch]
            ptr.is_word_end = True
        return self.__method1(0, s)
        #return self.__method2(s)
