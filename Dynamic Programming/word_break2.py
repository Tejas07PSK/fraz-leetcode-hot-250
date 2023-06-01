class TrieNode:
    def __init__ (self):
        self.chr = ''
        self.children = {}
        self.is_word_end = False

class Solution:
    def __wordBreakHelper (self, i, s):
        if (i == len(s)): return [True, []]
        if (self.dp[i] != None): return self.dp[i]
        self.dp[i] = [False, []]
        ptr = self.trie_root
        for j in range(i, len(s)):
            if (s[j] not in ptr.children): break
            ptr = ptr.children[s[j]]
            if (ptr.is_word_end):
                can_form_sen, sen_list = self.__wordBreakHelper(j + 1, s)
                if (can_form_sen):
                    self.dp[i][0] = True
                    curr_word = s[i:j+1]
                    if sen_list:
                        for sen in sen_list: self.dp[i][1].append(" ".join([curr_word, sen]))
                    else: self.dp[i][1].append(curr_word)
        return self.dp[i]

    def wordBreak (self, s: str, wordDict: List[str]) -> List[str]:
        self.trie_root = TrieNode()
        self.dp = [None for i in range(len(s))]
        for word in wordDict:
            ptr = self.trie_root
            for ch in word:
                if (ch not in ptr.children):
                    temp_trie_node = TrieNode()
                    temp_trie_node.chr = ch 
                    ptr.children[ch] = temp_trie_node
                ptr = ptr.children[ch]
            ptr.is_word_end = True
        return self.__wordBreakHelper(0, s)[1]
