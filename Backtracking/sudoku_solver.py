class Solution:
    def __resolveSubBox (self, row, col):
        if (0 <= row <= 2):
            if (0 <= col <= 2): return 0
            if (3 <= col <= 5): return 1
            if (6 <= col <= 8): return 2
        if (3 <= row <= 5):
            if (0 <= col <= 2): return 3
            if (3 <= col <= 5): return 4
            if (6 <= col <= 8): return 5
        if (6 <= row <= 8):
            if (0 <= col <= 2): return 6
            if (3 <= col <= 5): return 7
            if (6 <= col <= 8): return 8

    def __move (self, row, col):
        if ((row % 2) != 0):
            if (col == 0): return row + 1, col
            return row, col - 1
        else:
            if (col == 8): return row + 1, col
            return row, col + 1

    def __helper (self, row, col, board):
        if (row == 9): return True if (col == 8) else False
        sub_box_idx = self.__resolveSubBox(row, col)
        res = False
        if (board[row][col] != '.'): res = self.__helper(*self.__move(row, col), board)
        else:
            for i in map(str, range(1, 10)):
                if ((i not in self.row_set[row]) and (i not in self.col_set[col]) and (i not in self.sub_box_set[sub_box_idx])):
                    self.row_set[row].add(i)
                    self.col_set[col].add(i)
                    self.sub_box_set[sub_box_idx].add(i)
                    board[row][col] = i
                    res = self.__helper(*self.__move(row, col), board)
                    if (res): break
                    self.row_set[row].remove(i)
                    self.col_set[col].remove(i)
                    self.sub_box_set[sub_box_idx].remove(i)
                    board[row][col] = '.'
        return res


    def solveSudoku (self, board: List[List[str]]) -> None:
        self.col_set = [set() for i in range(9)]
        self.row_set = [set() for i in range(9)]
        self.sub_box_set = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                if (board[row][col] != '.'):
                    self.row_set[row].add(board[row][col])
                    self.col_set[col].add(board[row][col])
                    self.sub_box_set[self.__resolveSubBox(row, col)].add(board[row][col])
        self.__helper(0, 0, board)
        return board
