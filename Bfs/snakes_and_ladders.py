from collections import deque

class Solution:
    def snakesAndLadders (self, board: List[List[int]]) -> int:
        snakes_n_ladders, count, n = {}, 1, len(board) * len(board[0])
        col, col_offset = 0, 1
        for row in range(len(board) - 1, -1, -1):
            while ((col < len(board[0])) if (col_offset == 1) else (col >= 0)):
                if (board[row][col] != -1): snakes_n_ladders[count] = board[row][col]
                count += 1 ; col += col_offset
            if (col_offset < 0): col_offset, col = 1, 0
            else: col_offset, col = -1, len(board[0]) - 1
        q, visited = deque([(1, 0)]), set([1])
        while (q):
            curr_idx, moves = q.popleft()
            if (curr_idx == n): return moves
            for offset in range(1, 7):
                next_idx = curr_idx + offset
                if (next_idx <= n):
                    if (next_idx in snakes_n_ladders): next_idx = snakes_n_ladders[next_idx]
                    if (next_idx not in visited):
                        q.append((next_idx, moves + 1))
                        visited.add(next_idx)
        return -1
