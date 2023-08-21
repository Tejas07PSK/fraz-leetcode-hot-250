class Solution:
    def solve (self, board: List[List[str]]) -> None:
        stk, visited, dirs = deque(), set(), [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(board[0])):
            if (board[0][i] == 'O'):
                board[0][i] = -1
                stk.append((0, i))
                visited.add((0, i))
            if (board[-1][i] == 'O'):
                board[-1][i] = -1
                stk.append((len(board) - 1, i))
                visited.add((len(board) - 1, i))
        for i in range(len(board)):
            if (board[i][0] == 'O'):
                board[i][0] = -1
                stk.append((i, 0))
                visited.add((i, 0))
            if (board[i][-1] == 'O'):
                board[i][-1] = -1
                stk.append((i, len(board[0]) - 1))
                visited.add((i, len(board[0]) - 1))
        while (stk):
            curr_i, curr_j = stk.popleft()
            for i_offset, j_offset in dirs:
                next_i, next_j = curr_i + i_offset, curr_j + j_offset
                if ((0 <= next_i < len(board)) and (0 <= next_j < len(board[0]))):
                    if (((next_i, next_j) not in visited) and (board[next_i][next_j] == 'O')):
                        board[next_i][next_j] = -1
                        visited.add((next_i, next_j))
                        stk.append((next_i, next_j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == -1): board[i][j] = 'O'
                elif (board[i][j] == 'O'): board[i][j] = 'X'
