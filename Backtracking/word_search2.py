class TrieNode:
    def __init__ (self):
        self.ch = '*'
        self.children = {}
        self.is_word_end = False
        self.seen_before = False
        self.word = ""

class Solution:
    def __helper (self, row, col, trie_ptr, board):
        if ((trie_ptr.is_word_end) and (not trie_ptr.seen_before)):
            trie_ptr.seen_before = True
            self.res.append(trie_ptr.word)
        ch = board[row][col]
        board[row][col] = None
        for row_offset, col_offset in self.direcs:
            next_row, next_col = row + row_offset, col + col_offset
            if ((0 <= next_row < len(board)) and (0 <= next_col < len(board[0]))):
                next_chr = board[next_row][next_col]
                if ((next_chr) and (next_chr in trie_ptr.children)):
                    self.__helper(next_row, next_col, trie_ptr.children[next_chr], board)
        board[row][col] = ch

    def findWords (self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        self.res = []
        self.direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for word in words:
            ptr = root
            for ch in word:
                if (ch not in ptr.children):
                    tmp = TrieNode() ; tmp.ch = ch
                    ptr.children[ch] = tmp
                ptr = ptr.children[ch]
            ptr.is_word_end = True
            ptr.word = word
        for row in range(len(board)):
            for col in range(len(board[0])):
                ch = board[row][col]
                if (ch in root.children):
                    self.__helper(row, col, root.children[ch], board)
        return self.res
