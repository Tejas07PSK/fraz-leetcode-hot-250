class Solution:
    def __helper (self, i, j, k, board, word):
        if (k  == (len(word) - 1)): return True
        temp, board[i][j] = board[i][j], ''
        for i_offset, j_offset in self.dirs:
            next_i, next_j = i + i_offset, j + j_offset
            if ((0 <= next_i < len(board)) and (0 <= next_j < len(board[0])) and ((k + 1) < len(word)) and (board[next_i][next_j] == word[k + 1]) and (self.__helper(next_i, next_j, k + 1, board, word) == True)): return True
        board[i][j] = temp
        return False

    def exist (self, board: List[List[str]], word: str) -> bool:
        if ((len(board) * len(board[0])) < len(word)): return False
        wrd_freq = {}
        for ch in word:
            if (ch not in wrd_freq): wrd_freq[ch] = 0
            wrd_freq[ch] += 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] in wrd_freq):
                    wrd_freq[board[i][j]] -= 1
                    if (wrd_freq[board[i][j]] == 0): del wrd_freq[board[i][j]]
                if (not wrd_freq): break
            if (not wrd_freq): break
        if (wrd_freq): return False
        i, j = 0, len(word) - 1
        while (((i + 1) < len(word)) and (word[i] == word[i + 1])): i += 1
        while (((j - 1) >= 0) and (word[j] == word[j - 1])): j -= 1
        if ((i + 1) > (len(word) - j)): word = word[::-1]
        i, j = 0, 0
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if ((board[i][j] == word[0]) and (self.__helper(i, j, 0, board, word) == True)): return True
        return False
