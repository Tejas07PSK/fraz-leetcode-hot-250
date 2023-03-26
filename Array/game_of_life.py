class Solution:
    def gameOfLife (self, board: List[List[int]]) -> None:
        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                tot_live_nbs = 0
                for row_offset, col_offset in dirs:
                    next_row, next_col = row + row_offset, col + col_offset
                    if ((0 <= next_row < len(board)) and (0 <= next_col < len(board[0]))):
                        if ((board[next_row][next_col] % 2) == 1): tot_live_nbs += 1
                if (board[row][col] == 1):
                    if ((tot_live_nbs == 2) or (tot_live_nbs == 3)): board[row][col] += 2
                elif (tot_live_nbs == 3): board[row][col] += 2
        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] //= 2
