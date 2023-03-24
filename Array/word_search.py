class Solution:
    def __search (self, i, j, k, board, word):
        if (k == (len(word) - 1)): return True
        tmp = board[i][j]
        board[i][j] = ''
        for i_offset, j_offset in self.dirs:
            next_i, next_j = i + i_offset, j + j_offset
            if ((0 <= next_i < len(board)) and (0 <= next_j < len(board[0]))):
                if (((k + 1) < len(word)) and (word[k + 1] == board[next_i][next_j])):
                    if (self.__search(next_i, next_j, k + 1, board, word)): return True
        board[i][j] = tmp
        return False

    def exist (self, board: List[List[str]], word: str) -> bool:
        if ((len(board) * len(board[0])) < len(word)): return False
        freq_hm = {}
        for ch in word:
            if (ch not in freq_hm): freq_hm[ch] = 0
            freq_hm[ch] += 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] in freq_hm):
                    freq_hm[board[i][j]] -= 1
                    if (freq_hm[board[i][j]] == 0): del freq_hm[board[i][j]]
                if (not freq_hm): break
            if (not freq_hm): break
        if (freq_hm): return False
        i = 0
        while (((i + 1) < len(word)) and (word[i] == word[i + 1])): i += 1
        i += 1 ; j = len(word) - 1
        while (((j - 1) >= 0) and (word[j] == word[j - 1])): j -= 1
        j = len(word) - j
        if (i > j): word = word[::-1]
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == word[0]):
                    if (self.__search(i, j, 0, board, word)): return True
        return False
